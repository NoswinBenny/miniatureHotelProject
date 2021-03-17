import tkinter as tk
from tkinter import ttk


class Menu(tk.Frame):
    data = tuple()

    def __init__(self, parent, *args, **kwargs):
        super().__init__()
        menu_label = ttk.LabelFrame(
            master=parent, *args, **kwargs, text='Menu Card')

        frames_for_dishes = {
            'starter': ttk.LabelFrame(master=menu_label, text='Starter'),
            'mainCourse': ttk.LabelFrame(master=menu_label, text='Main Course'),
            'desert': ttk.LabelFrame(master=menu_label, text='Desert')
        }

        #  How to get the value out from state:
        #   -> this will give us the state of the button --> print(dishes['starter']['Water']['btn']['state'])
        #       and we can change the value of numbers using  onvalue=
        #           1st get the state of button:
        #               if Enabled then add value to the total

        var_for_each_dishes_of_starters = {
            #  tk.IntVar() -> stores int value
            'tea': tk.IntVar(),
            'idli': tk.IntVar(),
            'dosa': tk.IntVar(),
            'upttapa': tk.IntVar(),
            'poha': tk.IntVar(),
            'samosa': tk.IntVar(),
            'chapati&veg': tk.IntVar(),
            'coffee': tk.IntVar(),
        }

        var_for_each_dishes_of_main_course = {
            'choley': tk.IntVar(),
            'curry_in_hurry': tk.IntVar(),
            'chicken_biriyani': tk.IntVar(),
            'chana_dal_recipe': tk.IntVar(),
            'methi_matar_malai': tk.IntVar(),
            'tawa_panner': tk.IntVar(),
            'khatte_methe_baingan': tk.IntVar(),
            'punjabi_dum_aloo': tk.IntVar(),
            'rajma': tk.IntVar()
        }
        var_for_each_dishes_of_desert = {
            'gulab_jamun': tk.IntVar(),
            'rolled_chocolate_icecream': tk.IntVar(),
            'soft_cream_serve': tk.IntVar(),
            'frozen_yougurt': tk.IntVar(),
            'snow_cream': tk.IntVar(),
            'galato': tk.IntVar(),
            'kulfi': tk.IntVar(),
            'sorbet': tk.IntVar(),
            'cream_straberry': tk.IntVar()

        }

        dishes = {
            'starter': {

                "tea": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], onvalue=var_for_each_dishes_of_starters['tea'].set(10), text='Tea  Qty:', variable=var_for_each_dishes_of_starters['tea']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]

                },
                "idli": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], text='idli  Qty :', variable=var_for_each_dishes_of_starters['idli']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]

                },
                "dosa": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], text='Dosa  Qty :', variable=var_for_each_dishes_of_starters['dosa']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]

                },
                "upttapa": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], text='Upttapa  Qty :', variable=var_for_each_dishes_of_starters['upttapa']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]
                },
                "poha": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], text='Poha  Qty :', variable=var_for_each_dishes_of_starters['poha']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]
                },
                "samosa": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], text='Samosa  Qty :', variable=var_for_each_dishes_of_starters['samosa']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]
                },
                "chapati&veg": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], text='Chapati&veg  Qty :', variable=var_for_each_dishes_of_starters['chapati&veg']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]
                },
                "coffee": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['starter'], text='Coffee  Qty :', variable=var_for_each_dishes_of_starters['coffee']),
                    'qty': [ttk.Entry(master=frames_for_dishes['starter'], width=5), tk.IntVar()]
                }
            },
            'mainCourse': {

                "curry_in_hurry": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Curry In Hurry  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['curry_in_hurry']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                },
                "chicken_biriyani": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Chicken Biryani  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['chicken_biriyani']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                },
                "chana_dal_recipe": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Chana Dal  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['chana_dal_recipe']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                },
                "methi_matar_malai": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Methi Matar Malai  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['methi_matar_malai']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                },
                "tawa_panner": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Tawa Panner  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['tawa_panner']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                },
                "khatte_methe_baingan": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Khatte Methe Baingan  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['khatte_methe_baingan']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                },
                "punjabi_dum_aloo": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Punjabi Dum Aloo  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['punjabi_dum_aloo']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                },
                "rajma": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['mainCourse'], text='Rajma  Qty :', variable=var_for_each_dishes_of_main_course
                                           ['rajma']),
                    'qty': [ttk.Entry(master=frames_for_dishes['mainCourse'], width=5), tk.IntVar()]
                }


            },
            'desert': {

                "gulab_jamun": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Gulab Jamun   Qty :', variable=var_for_each_dishes_of_desert
                                           ['gulab_jamun']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                },
                "rolled_chocolate_icecream": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Rolled Chocolate Icecream  Qty :', variable=var_for_each_dishes_of_desert
                                           ['rolled_chocolate_icecream']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                },
                "soft_cream_serve": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Soft Cream Serve  Qty :', variable=var_for_each_dishes_of_desert
                                           ['soft_cream_serve']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                },
                "frozen_yougurt": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Frozon Yougurt  Qty :', variable=var_for_each_dishes_of_desert
                                           ['frozen_yougurt']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                },
                "galato": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Galato  Qty :', variable=var_for_each_dishes_of_desert
                                           ['galato']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                },
                "kulfi": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Kulfi  Qty :', variable=var_for_each_dishes_of_desert
                                           ['kulfi']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                },
                "sorbet": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Soebet  Qty :', variable=var_for_each_dishes_of_desert
                                           ['sorbet']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                },
                "cream_straberry": {
                    'btn': ttk.Checkbutton(master=frames_for_dishes['desert'], text='Cream berry  Qty :', variable=var_for_each_dishes_of_desert
                                           ['cream_straberry']),
                    'qty': [ttk.Entry(master=frames_for_dishes['desert'], width=5), tk.IntVar()]
                }

            }
        }

        # -------------------------------------------------------------------- Putting Starter's All the Buttons on the Window

        # result = list(map(lambda x: ,
        #   [dishes['starter']['idli']['btn'], dishes['starter']['idli']['qty'], dishes['starter']['Tea']['btn']]))[:]

        # setting all the values of qty

        dishes['starter']['idli']['btn'].grid(column=0, row=0, padx=5, pady=5)
        dishes['starter']['idli']['qty'][0].grid(column=1, row=0, padx=5, pady=5, )
        dishes['starter']['idli']['qty'][1].set(30)

        dishes['starter']['tea']['btn'].grid(column=2, row=0, padx=5, pady=5)
        dishes['starter']['tea']['qty'][0].grid(column=3, row=0, padx=5, pady=5)
        dishes['starter']['tea']['qty'][1].set(10)

        dishes['starter']['dosa']['btn'].grid(column=4, row=0, padx=5, pady=5)
        dishes['starter']['dosa']['qty'][0].grid(column=5, row=0, padx=5, pady=5)
        dishes['starter']['dosa']['qty'][1].set(40)

        dishes['starter']['upttapa']['btn'].grid(
            column=6, row=0, padx=5, pady=5)
        dishes['starter']['upttapa']['qty'][0].grid(
            column=7, row=0, padx=5, pady=5)
        dishes['starter']['upttapa']['qty'][1].set(60)

        dishes['starter']['poha']['btn'].grid(column=0, row=1, padx=5, pady=5)
        dishes['starter']['poha']['qty'][0].grid(column=1, row=1, padx=5, pady=5)
        dishes['starter']['poha']['qty'][1].set(20)

        dishes['starter']['samosa']['btn'].grid(
            column=2, row=1, padx=5, pady=5)
        dishes['starter']['samosa']['qty'][0].grid(
            column=3, row=1, padx=5, pady=5)
        dishes['starter']['samosa']['qty'][1].set(10)

        dishes['starter']['chapati&veg']['btn'].grid(
            column=4, row=1, padx=5, pady=5)
        dishes['starter']['chapati&veg']['qty'][0].grid(
            column=5, row=1, padx=5, pady=5)
        dishes['starter']['chapati&veg']['qty'][1].set(50)

        dishes['starter']['coffee']['btn'].grid(
            column=6, row=1, padx=5, pady=5)
        dishes['starter']['coffee']['qty'][0].grid(
            column=7, row=1, padx=5, pady=5)
        dishes['starter']['coffee']['qty'][1].set(20)
        # ---------------------------------------------------------------------------------- Putting MainCourser's All the Buttons on the Window
        dishes['mainCourse']['chicken_biriyani']['btn'].grid(
            column=0, row=0, padx=5, pady=5)
        dishes['mainCourse']['chicken_biriyani']['qty'][0].grid(
            column=1, row=0, padx=5, pady=5)
        dishes['mainCourse']['chicken_biriyani']['qty'][1].set(160)

        dishes['mainCourse']['curry_in_hurry']['btn'].grid(
            column=2, row=0, padx=5, pady=5)
        dishes['mainCourse']['curry_in_hurry']['qty'][0].grid(
            column=3, row=0, padx=5, pady=5)
        dishes['mainCourse']['curry_in_hurry']['qty'][1].set(130)

        dishes['mainCourse']['chana_dal_recipe']['btn'].grid(
            column=4, row=0, padx=5, pady=5)
        dishes['mainCourse']['chana_dal_recipe']['qty'][0].grid(
            column=5, row=0, padx=5, pady=5)
        dishes['mainCourse']['chana_dal_recipe']['qty'][1].set(190)

        dishes['mainCourse']['methi_matar_malai']['btn'].grid(
            column=6, row=0, padx=5, pady=5)
        dishes['mainCourse']['methi_matar_malai']['qty'][0].grid(
            column=7, row=0, padx=5, pady=5)
        dishes['mainCourse']['methi_matar_malai']['qty'][1].set(650)

        dishes['mainCourse']['tawa_panner']['btn'].grid(
            column=0, row=1, padx=5, pady=5)
        dishes['mainCourse']['tawa_panner']['qty'][0].grid(
            column=1, row=1, padx=5, pady=5)
        dishes['mainCourse']['tawa_panner']['qty'][1].set(230)

        dishes['mainCourse']['khatte_methe_baingan']['btn'].grid(
            column=2, row=1, padx=5, pady=5)
        dishes['mainCourse']['khatte_methe_baingan']['qty'][0].grid(
            column=3, row=1, padx=5, pady=5)
        dishes['mainCourse']['khatte_methe_baingan']['qty'][1].set(150)

        dishes['mainCourse']['punjabi_dum_aloo']['btn'].grid(
            column=4, row=1, padx=5, pady=5)
        dishes['mainCourse']['punjabi_dum_aloo']['qty'][0].grid(
            column=3, row=1, padx=5, pady=5)
        dishes['mainCourse']['punjabi_dum_aloo']['qty'][1].set(200)

        dishes['mainCourse']['rajma']['btn'].grid(
            column=6, row=1, padx=5, pady=5)
        dishes['mainCourse']['rajma']['qty'][0].grid(
            column=7, row=1, padx=5, pady=5)
        dishes['mainCourse']['rajma']['qty'][1].set(566)

        # ------------------------------------------------------------------Putting Desert's All the Buttons on the Window
        dishes['desert']['gulab_jamun']['btn'].grid(
            column=0, row=0, padx=5, pady=5)
        dishes['desert']['gulab_jamun']['qty'][0].grid(
            column=1, row=0, padx=5, pady=5)

        dishes['desert']['rolled_chocolate_icecream']['btn'].grid(
            column=2, row=0, padx=5, pady=5)
        dishes['desert']['rolled_chocolate_icecream']['qty'][0].grid(
            column=3, row=0, padx=5, pady=5)

        dishes['desert']['soft_cream_serve']['btn'].grid(
            column=4, row=0, padx=5, pady=5)
        dishes['desert']['soft_cream_serve']['qty'][0].grid(
            column=5, row=0, padx=5, pady=5)

        dishes['desert']['frozen_yougurt']['btn'].grid(
            column=6, row=0, padx=5, pady=5)
        dishes['desert']['frozen_yougurt']['qty'][0].grid(
            column=7, row=0, padx=5, pady=5)

        dishes['desert']['galato']['btn'].grid(column=0, row=1, padx=5, pady=5)
        dishes['desert']['galato']['qty'][0].grid(column=1, row=1, padx=5, pady=5)

        dishes['desert']['kulfi']['btn'].grid(column=2, row=1, padx=5, pady=5)
        dishes['desert']['kulfi']['qty'][0].grid(column=3, row=1, padx=5, pady=5)

        dishes['desert']['sorbet']['btn'].grid(column=4, row=1, padx=5, pady=5)
        dishes['desert']['sorbet']['qty'][0].grid(column=5, row=1, padx=5, pady=5)

        dishes['desert']['cream_straberry']['btn'].grid(
            column=6, row=1, padx=5, pady=5)
        dishes['desert']['cream_straberry']['qty'][0].grid(
            column=7, row=1, padx=5, pady=5)

        # columnconfigure in my opinion allows the elements to expand.
        # frames_for_dishes['starter'].columnconfigure(0, weight=1)
        frames_for_dishes['starter'].grid(padx=5, pady=5, sticky='we')
        frames_for_dishes['mainCourse'].grid(padx=5, pady=5, sticky='we')
        frames_for_dishes['desert'].grid(padx=5, pady=5, sticky='we')

        def return_bill():
            result_of_starters = filter(lambda x: x if x[1].get() == 1 else None, list(
                var_for_each_dishes_of_starters.items()))

            result_of_main_course = filter(lambda x: x if x[1].get() == 1 else None, list(
                var_for_each_dishes_of_main_course.items())) 

            result_of_desert = filter(lambda x: x if x[1].get() == 1 else None, list( 
                var_for_each_dishes_of_desert.items()
            ))
            print('>', dishes['starter']['tea']['qty'][0].get())

            total_of_starters = []
            for values in list(result_of_starters):
                entry_value = dishes['starter'][values[0]]['qty'][0].get()
                item_value = dishes['starter'][values[0]]['qty'][1].get()
                # the error invalid error tells us that the when entry_value is empty then there is problem to convert value in to int becoz it's None
                if entry_value:
                    if int(entry_value) > 0:
                        total_of_starters.append(int(entry_value) * item_value)
                    else:
                        total_of_staters.append(item_value)
                else:
                    total_of_starters.append(item_value)
            print("starter_bill", total_of_starters)

            total_of_main_course = []
            for values in list(result_of_main_course):
                entry_value = dishes['mainCourse'][values[0]]['qty'][0].get()
                item_value = dishes['mainCourse'][values[0]]['qty'][1].get()

                # the error invalid error tells us that the when entry_value is empty then there is problem to convert value in to int becoz it's None

                if entry_value:
                    if int(entry_value) > 0:
                        total_of_main_course.append(int(entry_value) * item_value)
                    else:
                        total_of_main_course.append(item_value)
                else:
                    total_of_main_course.append(item_value)
            print('main_course_bill', total_of_main_course)

            total_of_desert = []
            for values in list(result_of_desert):
                entry_value = dishes['desert'][values[0]]['qty'][0].get()
                item_value = dishes['desert'][values[0]]['qty'][1].get()

                # the error invalid error tells us that the when entry_value is empty then there is problem to convert value in to int becoz it's None
                print(entry_value)
                if entry_value:
                    if int(entry_value) > 0:
                        total_of_desert.append(int(entry_value) * item_value)
                    else:
                        total_of_desert.append(item_value)
                else:
                    total_of_desert.append(item_value)
            print('desert', total_of_desert)

            starter_bill = sum(total_of_starters)
            main_course_bill = sum(total_of_main_course)
            desert_bill = sum(total_of_desert)

            total = starter_bill + main_course_bill + desert_bill
            Menu.data = total

        button = ttk.Button(master = menu_label,
                            text = 'Confirm', command = return_bill)
        button.grid()

        menu_label.columnconfigure(0, weight = 1)
        menu_label.grid(padx = 5, pady = 5, sticky = 'nsew')



    @staticmethod
    def give_data():
        return Menu.data


# root, width=5 = tk.Tk()
# Menu(root, width=50, height=30).grid_columnconfigure(0, weight=1)
# root.geometry('400x400')
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# root.mainloop()



