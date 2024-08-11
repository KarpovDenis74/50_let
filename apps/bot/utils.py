import requests
import json
from time import sleep


class YangexGPT():
    def __init__(self, question: str, assistant) -> None:
        self.question = question
        self.assistant = assistant

    def _get_token(self, token: str) -> str:
        return (json.loads(
            requests.post(
                'https://iam.api.cloud.yandex.net/iam/v1/tokens',
                data=json.dumps({'yandexPassportOauthToken': f'{token}'}))
            .text)['iamToken'])

    def _get_headers(self, iam_token: str, folder: str) -> dict:
        return {'Content-Type': 'application/json',
                'Authorization': f'Bearer {iam_token}',
                'x-folder-id': folder}

    def _get_data(self, temperature, maxTokens, role, folder, question):
        return (json.dumps(
            {'modelUri': f'gpt://{folder}/yandexgpt-lite',
             'completionOptions': {'stream': False,
                                   'temperature': f'{temperature}',
                                   'maxTokens': f'{maxTokens}'},
             'messages': [
                {'role': 'system',
                 'text': f'{role}'},
                {'role': 'user',
                 'text': f'{question}'}
                ]
             }
        ))

    def _get_response(self, headers, data):
        return (
            requests.post('https://llm.api.cloud.yandex.net/'
                          'foundationModels/v1/completionAsync',
                          headers=headers, data=data)
        )

    def _get_answer_for_response(self, response, iam_token):
        if response.status_code == 200:
            answer = json.loads(response.text)
            print(f'{answer=}')
            id = answer["id"]
            while not answer['done']:
                headers = {'Authorization': f'Bearer {iam_token}'}
                response = requests.get(
                    f'https://llm.api.cloud.yandex.net/operations/{id}',
                    headers=headers
                )
                answer = json.loads(response.text)
                sleep(3)
                print(f'{      type(answer)=}')
        else:
            return ''
        print(f'{           type(answer)=}')
        print(f'{           answer=}')
        return answer['response']['alternatives'][0]['message']['text']

    def get_answer(self):
        iam_token = self._get_token(self.assistant.token)
        headers = self._get_headers(iam_token, self.assistant.folder)
        data = self._get_data(self.assistant.temperature,
                              self.assistant.max_tokens,
                              self.assistant.role,
                              self.assistant.folder,
                              self.question)

        response = self._get_response(headers, data)
        answer = self._get_answer_for_response(response, iam_token)
        return answer


class AssistantUtils():
    type = {'Yandex GPT': 'YangexGPT'}

    def __init__(self, assistant):
        self.assistant = assistant

    def _get_assistant_type(self):
        return self.assistant.type_gpt

    def get_answer(self, question: str) -> str:
        print(f'{self.assistant=}')
        if self.assistant.type_gpt.name == 'Yandex GPT':
            gpt = YangexGPT(question, self.assistant)
            return gpt.get_answer()
        else:
            return ''
