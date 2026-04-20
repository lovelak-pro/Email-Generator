import webview
import secrets
import os


class APP:
    def main(self,amount):
        print(amount)
        for r in range(1, amount+1):
            random_hex = secrets.token_hex(5)
            if not os.path.isdir('GENERATED_EMAILS'):
                os.system('mkdir GENERATED_EMAILS')
            with open(f'GENERATED_EMAILS\\Gmail_{r}.txt', 'w') as login_details:
                login_details.write('Email : '+str(random_hex)+f'@gmail.com\nPassword : {random_hex[::-1]}')


if __name__ == "__main__":
    app = APP()
    webview.create_window('Email Generator','src/index.html',width=350,height=190,resizable=False,js_api=app)
    webview.start()