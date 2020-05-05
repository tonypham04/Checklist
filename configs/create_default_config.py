import configparser

config = configparser.ConfigParser()

# CONFIGURATIONS FOR THE BANNER CLASS
config['BANNER'] = {'banner_width': 480,
                    'banner_height': 180,
                    'banner_text': 'Be Yourself',
                    'banner_background_color': '#008004',
                    'banner_text_color': '#ffffff',
                    'banner_font': 'Impact',
                    'banner_font_size': 64}

# WRITE CONFIGURATIONS TO A FILE
with open('config.ini', 'w') as configfile:
    config.write(configfile)