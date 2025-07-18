from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from datetime import datetime
import json
import os

def load_json(file):
    with open(file, encoding='utf-8') as f:
        return json.load(f)

def load_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as f:
            return json.load(f)
    return []

def save_transaction(entry):
    data = load_transactions()
    data.append(entry)
    with open("transactions.json", "w") as f:
        json.dump(data, f)

def load_currency():
    data = load_json("currency.json")
    try:
        config = load_json("config.json")
        selected = config.get("currency", "USD")
    except:
        selected = "USD"
    for cur in data["currencies"]:
        if cur["code"] == selected:
            return cur
    return data["currencies"][0]

def set_currency(code):
    with open("config.json", "w") as f:
        json.dump({"currency": code}, f)

lang = load_json("lang.json")
currency = load_currency()

class HomeScreen(Screen):
    def update_balance(self):
        global currency
        currency = load_currency()
        data = load_transactions()
        income = sum(x['amount'] for x in data if x['type'] == 'income')
        expense = sum(x['amount'] for x in data if x['type'] == 'expense')
        balance = income - expense
        self.ids.balance_label.text = f"{lang['balance']}: {currency['symbol']}{balance}"

    def open_currency_popup(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        currencies = load_json("currency.json")["currencies"]

        popup = Popup(title="Select Currency", size_hint=(0.8, 0.8))

        for cur in currencies:
            btn = Button(text=f"{cur['name']} ({cur['symbol']})", size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn, code=cur["code"]: self.set_new_currency(code, popup))
            layout.add_widget(btn)

        popup.content = layout
        popup.open()

    def set_new_currency(self, code, popup):
        set_currency(code)
        popup.dismiss()
        self.update_balance()

    def on_pre_enter(self, *args):
        self.update_balance()

class AddTransactionScreen(Screen):
    def add_transaction(self):
        try:
            desc = self.ids.desc_input.text
            amount = float(self.ids.amount_input.text)
            trans_type = self.ids.type_spinner.text.lower()
            date = datetime.now().strftime("%Y-%m-%d %H:%M")
            save_transaction({"desc": desc, "amount": amount, "type": trans_type, "date": date})
            self.ids.desc_input.text = ""
            self.ids.amount_input.text = ""
            self.manager.current = 'home'
        except:
            pass

class ViewTransactionsScreen(Screen):
    def on_pre_enter(self, *args):
        self.ids.trans_label.text = ""
        data = load_transactions()
        if not data:
            self.ids.trans_label.text = lang['no_data']
        for item in data[-10:]:
            line = f"{item['date']} - {item['type'].capitalize()} - {currency['symbol']}{item['amount']} - {item['desc']}"
            self.ids.trans_label.text += line + "\n"

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("finance.kv")

class FinanceApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    FinanceApp().run()
