import webbrowser
from simple_colors import *
from termcolor import colored


lpresets = {'youtube search' : '/results?search_query='}


def websearch():
    helpbypass = 0
    while helpbypass == 0:
        sthelp = input('\n help(y/n): ')
        if sthelp == 'y':
            def help():
                print(colored('\n ' + '''This is a program that lets you open sites from the terminal. 

                        -----------------------------------------------------------------------------------

                        You will have a series of options, 1: Help, 2: Web protocol, 3: Presets, 4: Page url:

                        1: Help is what you are in right now, help can only be called in the beginning. 

                        2: A protocol is a standard set of rules that allow electronic devices to communicate with each other, in other words, if you dont insert a protocol at this stage, the program
                        will not work, do 'protohelp' if you want to choose a protocol, note: some protocols might not work for certain sites. 

                        3: You can use already typed presets to make you're searching faster, you can choose to use then or not. 

                        4: Insert the page url here, without the protocol since it (the protocol) will be added in the end, making the program work, dont forget the .com or .org, ect.
                        | ex: 'nameOfSite.com/org ect'. |

                        -------------------------------------------------------------------------------------''', 'cyan'))
                        

                helpdone = input(colored('\n ❔ done reading (press any key) ❔: ', 'cyan', attrs=['underline']))
                if helpdone:
                    pass
            help()
            helpbypass = 1
        elif sthelp == 'n':
            print(colored(' ✅ help was not provided ✅', 'green'))
            helpbypass = 1
        else:
            print(colored(f' ❌ {sthelp} is not a valid answer ❌', 'red'))
            pass
    def protoweb():
        protobypass = 0
        while protobypass == 0:
            global protocol
            protocol = input('\n web protcol(do protohelp for help on valied protocols): ')
            if protocol == '':
                print(colored('\n ❌ please enter web protocol ❌', 'red'))
                protobypass = 0
            elif protocol == 'protohelp':
                print(colored('\n valid protocols (type these as they are here): \n http:/, https:/, www., dns. \n NOTE: some of these might not work on specific sites.', 'yellow', attrs=['underline']))
                protobypass = 0
            else:
                protobypass = 1
                print(colored(f' ✅ {protocol} protocol chosen ✅', 'green'))
                pass

            if protobypass == 1:
                def presets():
                    presetbypass = 0
                    presetchoosen = 0
                    while presetbypass == 0:
                        preset = input('\n presets(y/n): ')
                        if preset == '':
                            print(colored(f'\n ❌ {preset} is not a valid answer, please type a valid answer ❌', 'red'))
                            presetbypass = 0
                            presetchoosen = 0
                        if preset == 'y':
                            askprebypass = 0
                            while askprebypass == 0:
                                listprint = [(key) for key in lpresets.keys()]
                                global askpre
                                askpre = input(colored(f'\n name of presets:' + '\n' + str(colored(' '+', '.join(listprint)+ ' ', 'magenta', attrs=['underline', 'bold'])) + '\n preset: ', 'magenta'))
                                if askpre not in lpresets.keys():
                                    print(colored(f'\n ❌ sorry, this preset does not exist \n choose another one ❌: ', 'red'))
                                    presetbypass = 1
                                    askprebypass = 0
                                    presetchoosen = 0        

                                elif askpre in lpresets.keys():
                                    textAskpre = askpre
                                    #-
                                    if askpre == 'youtube search':
                                        askpre = 0
                                        global search
                                        search = input(colored('\n what do you want to search: ', 'magenta', attrs=['bold']))

                                    #-
                                    print(colored(f' ✅ {textAskpre} chosen ✅', 'magenta', attrs=['dark']))
                                    values = lpresets.values()
                                    valuesList = list(values)
                                    global addPreset
                                    addPreset = valuesList[askpre]
                                    
                                    presetbypass = 1
                                    askprebypass = 1
                                    presetchoosen = 1

                        elif preset == 'n':
                            print(colored(' ✅ no preset chosen ✅', 'green'))
                            addPreset = ''
                            search = ''
                            presetbypass = 1
                            presetchoosen = 0
                            pass
                        
                        else:

                            print(colored('\n ❌ {preset} is not a valid answer, please type a valid answer ❌', 'red'))
                            presetbypass = 0
                            presetchoosen = 0
                             

                presets()

                
                global page
                page = input(colored('\n page url: ', 'yellow', attrs=['bold']))
            else:
                protobypass = 0
                pass
        webbrowser.open(str(protocol + page + addPreset + search))
        print(colored('✅ program executed successfully ✅', 'green' , attrs= ['bold']))

    protoweb()

websearch()