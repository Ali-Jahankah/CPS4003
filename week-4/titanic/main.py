
import tui,process

records = []
def run():
    global records
    tui.welcome()
    while True:
        
        chosenOption= tui.main_menu()
        if chosenOption in range(1,5):
            if chosenOption == 1:
                tui.progress("Data loading",0)
                file_path = tui.data_file_path()
                records= process.load_data(file_path) #./week-4/titanic/data/titanic.csv
                tui.progress("COMPLETED",100)
            elif chosenOption == 2:
                while True:
                    tui.progress("Data Processing",0)
                    process_chosen = tui.process_menu()
                    if process_chosen == 1:
                        names =process.extract_passengers(records)
                        tui.display_passenger_names(names)
                        break
                    elif process_chosen == 2:
                        counts = process.count_survivors(records)
                        tui.display_survivor_count(counts)
                        break
                    elif process_chosen == 3:
                        count_per_sex = process.count_per_sex(records)
                        tui.display_sex_counts(count_per_sex)
                        break
                    elif process_chosen == 4:
                        age= process.count_per_age_group(records)
                        tui.display_age_group_counts(age)
                        break
                    elif process_chosen == 5:
                        break
                tui.progress("COMPLETED",100)
            elif chosenOption == 3:
                tui.progress("Data visualising",0)
                chosen_visualise_option = tui.visual_menu()
                if chosen_visualise_option == 1:
                    data = process.per_class_count(records)
                    print(data)
                    tui.display_visual(data)
        else:
            print("\nPlease choose a valid option!\n")
        
        # Task: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the tui module to indicate that data visualisation has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the tui module to indicate that data visualisation has completed.
        #
        # To visualise the data, do the following:
        # - Use the appropriate function in the tui module to display a menu of options for visualising the data.
        # - Check which option has been selected and do the following for the selected option:
        #   - Use the appropriate function in the tui module indicate that the process has started.
        #   - Add an appropriate function in the process module and use it to retrieve the data to be visualised.
        #   - Use the appropriate function in the visual module to generate the visualisation.
        #   - Use the appropriate function in the tui module to display the visualisation.
        #   - Use the appropriate function the tui module to indicate the selection operation has completed.
        # TODO: Your code here

        # Task: Check if the user selected the option for exiting.  If so, break out of the loop.
        # TODO: Your code here

        # Task: If the user selected an invalid option then use the appropriate function in the tui module to
        # display an error message
        # TODO: Your code here (remove pass below)
        pass


if __name__ == "__main__":
    run()
