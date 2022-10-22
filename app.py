from flask import Flask
from flask import request, render_template

 
app = Flask(__name__)
 
@app.route('/')

def index():

   name = 'Anya'
   surname = 'Kostyuchenko'
   avatar = '/static/assets/avatar (1).png'

   line_chart_legend = [{'name':'Offline orders', 'dot':'dot_1'},
                        {'name':'Online orders', 'dot':'dot_2'}]

   circle_chart_legend = [{'name':'Offline', 'dot':'dot_3'},
                          {'name':'Online', 'dot':'dot_2'},
                          {'name':'Trade', 'dot':'dot_1'}]



   cards = [{'total_number':'89,935', 'kpi':'Total users', 'icon':'/static/assets/icon.png', 'bottom_text':'+1.01% this week', 'bottom_number':'10.2', 'bottom_icon':'/static/assets/up.png'},
            {'total_number':'23,283.5', 'kpi':'Total products', 'icon':'/static/assets/icon.png', 'bottom_text':'+0.49% this week', 'bottom_number':'3.1', 'bottom_icon':'/static/assets/up.png'},
            {'total_number':'46,827', 'kpi':'Total users', 'icon':'/static/assets/icon.png', 'bottom_text':'-0.91% this week', 'bottom_number':'2.56', 'bottom_icon':'/static/assets/shape (10).png'},
            {'total_number':'124,854', 'kpi':'Refunded', 'icon':'/static/assets/icon.png', 'bottom_text':'+1.51% this week', 'bottom_number':'7.2', 'bottom_icon':'/static/assets/up.png'}]

   left_bottom_menu = [{'name':'Help Centre', 'icon' : '/static/assets/info.png'},
                        {'name':'Contact us','icon' : '/static/assets/chat.png'},
                        {'name':'Log out','icon' : '/static/assets/shape (11).png'}]


   left_menu = [{'name':'Overview','icon':'/static/assets/chart (14).png', 'expand': False, 'number':False},
                {'name':'Product','icon':'/static/assets/case.png','expand': True, 'number':False},
                {'name':'Orders','icon':'/static/assets/user.png','expand': True, 'number':False},
                {'name':'Checkout','icon':'/static/assets/checkout.png','expand': False, 'number':2},
                {'name':'Setting','icon':'/static/assets/settings.png','expand': False, 'number':False}]

   return  render_template('index.html', name = name, surname = surname, left_menu = left_menu, left_bottom_menu = left_bottom_menu, avatar = avatar, cards = cards, circle_chart_legend = circle_chart_legend, line_chart_legend = line_chart_legend)

if __name__ == "__main__":
    app.run(debug = True)