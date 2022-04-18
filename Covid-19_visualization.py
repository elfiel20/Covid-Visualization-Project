# Programming Assignment 2 by enmity

# import necessary modules
import pygame
import color
import pygame_helper
import covid_data

# initialize pygame window and fill w/ color
pygame.init()
w = 600
h = 400
win = pygame.display.set_mode((w,h))
win.fill(color.back_pink)

# update display accordingly
pygame.display.update()


# user input
state = input("Enter a state: ")

# check for is
# the user entered a valid state
if covid_data.valid_state(state):
    # true == valid state
    print("State is a valid state.")
else: print("State is not a valid state.", pygame_helper.wait_for_quit())


# Cases or Deaths
answer = input("Would you like data based on Covid-19 deaths or cases? Enter 1 for deaths and 2 for cases: ")
pygame_helper.wait_for_click()
if answer == 1:
    for i in range(covid_data.num_entries(state)//2):
        # dividing numbers of entries in half for "split dye" effect on color of data points in window
        # Meaning halfway through the entries the color changes
        # i = id for entry
        # Deaths by date
        date = covid_data.date_by_entry_id(state, i)
        deaths = covid_data.deaths_by_entry_id(state, i)
        covid_data.num_entries(state)
        x = i * w // covid_data.num_entries(state)
        y = h - (deaths * h // covid_data.deaths_by_entry_id(state, covid_data.num_entries(state) - 1))
        x = i * w // covid_data.num_entries(state)
        y = h - (deaths * h // covid_data.deaths_by_entry_id(state, covid_data.num_entries(state) - 1))
        # win.set_at((x,y), color.pinkp)
        pygame.draw.circle(win, color.pink, (x, y), 1)

        for i in range(covid_data.num_entries(state) // 2), covid_data.num_entries(state) :
            # dividing numbers of entries in half to start after the previous for loop is finished
            # same structure for cases
            # i = id for entry
            # Deaths by date
            date = covid_data.date_by_entry_id(state, i)
            deaths = covid_data.deaths_by_entry_id(state, i)
            covid_data.num_entries(state)
            x = i * w // covid_data.num_entries(state)
            y = h - (deaths * h // covid_data.deaths_by_entry_id(state, covid_data.num_entries(state) - 1))
            x = i * w // covid_data.num_entries(state)
            y = h - (deaths * h // covid_data.deaths_by_entry_id(state, covid_data.num_entries(state) - 1))
            # win.set_at((x,y), color.pinkp)
            pygame.draw.circle(win, color.pink, (x, y), 1)


else:
    for i in range((covid_data.num_entries(state)//2)):
        # i = id for entry
        # cases by date
        date = covid_data.date_by_entry_id(state, i)
        cases = covid_data.cases_by_entry_id(state, i)
        x = i * w // covid_data.num_entries(state)
        y = h - (cases * h // covid_data.cases_by_entry_id(state, covid_data.num_entries(state) -1))

        pygame.draw.circle(win, color.pink, (x,y), 1)
        for i in range((covid_data.num_entries(state)//2), covid_data.num_entries(state)):
            # i = id for entry
            # cases by date
            date = covid_data.date_by_entry_id(state, i)
            cases = covid_data.cases_by_entry_id(state, i)
            x = i * w // covid_data.num_entries(state)
            y = h - (cases * h // covid_data.cases_by_entry_id(state, covid_data.num_entries(state) - 1))
            pygame.draw.circle(win, color.purple, (x, y), 1)


# adding text to window
# create a font object
font = pygame.font.SysFont("Veranda", 40)

# render some text into a new surface
# True means enable anti aliasing to smooth the edges of the text

msg = font.render("Covid-19 Visualization", True, color.dusty_rose)

# blit our message onto the window ----> centered
msg_width = msg.get_width()
msg_height = msg.get_height()
# adjust x and y to make the text appear in the top left quadrant
msg_x = w // 6 - msg_width // 6
msg_y = msg_height
win.blit(msg, (msg_x, msg_y))



pygame.display.update()
pygame_helper.wait_for_quit()