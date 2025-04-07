import json

class Config:
    def __init__(self):
        self.settings = {
            "game_rules": {
                "blackjack_payout": 1.5,
                "dealer_hits_on_soft_17": True,
                "max_players": 6,
                "min_bet": 10,
                "max_bet": 1000
            },
            "player_settings": {
                "default_bankroll": 500,
                "allow_splitting": True,
                "allow_doubling": True
            },
            "ui_settings": {
                "theme": "dark",
                "font_size": 14,
                "show_card_values": True
            }
        }
        self.load_config()

    def load_config(self):
        try:
            with open('config.json', 'r') as config_file:
                self.settings = json.load(config_file)
        except FileNotFoundError:
            self.save_config()  # Create a default config if not found

    def save_config(self):
        with open('config.json', 'w') as config_file:
            json.dump(self.settings, config_file, indent=4)

    def get_setting(self, key):
        keys = key.split('.')
        value = self.settings
        for k in keys:
            value = value.get(k, None)
            if value is None:
                break
        return value

    def set_setting(self, key, value):
        keys = key.split('.')
        setting = self.settings
        for k in keys[:-1]:
            setting = setting.setdefault(k, {})
        setting[keys[-1]] = value
        self.save_config()