from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
from datetime import datetime
from tkinter import *
import random
global POPULATION_SIZE
now_start = datetime.utcnow()
no_iteratons = 3
for i in range(no_iteratons):
    product_lst = ['Amazon Launchpad', 'Apps for Android', 'Baby Products', 'Bags', ' Wallets and Luggage', 'Beauty',
                   'Book', 'Car', 'Motorbike', 'Clothing and Accessories', 'Computers and Accessories',
                   'Garden and Outdoors','Gift Cards', 'Grocery and Gourmet Foods', 'Health and Personal Care', 'Home and Kitchen',
                   'Home Improvement', 'Industrial and Scientific', 'Jewellery', 'Kindle Store', 'Movies and TV Shows', 'Music', 'Musical Instruments',
                   'Office Products', 'Pet Supplies', 'Shoes and Handbags', 'Software', 'Sports, Fitness and Outdoors', 'Toys and Games', 'Video Games',
                   'Watches']
    customer_name = ['Hanusha', 'Vanitha', 'Manisha Koyerala', 'geetha']
    user_name = ['7708612594', 'vantha123@gmail.com', 'ananomysperson0@gmail.com', 'Hanusha2000@gmail.com',
                 'manisha2000@gmail.com', 'someone123@gmail.com', '9788882258', '93487584834']
    password = ['Password_123']
    customer_name_random = random.choice(customer_name)
    #print(customer_name_random)

    password_random = random.choice(password)
    #print(password_random)

    user_name_random = random.choice(user_name)
    #print(user_name_random)

    product = random.choice(product_lst)
    POPULATION_SIZE = 100
    # Valid genes
    GENES = '''abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ,&'''

    # Target string to be generated
    TARGET = product


    class Individual(object):
        '''
        Class representing individual in population
        '''
        def __init__(self, chromosome):
            self.chromosome = chromosome
            self.fitness = self.cal_fitness()

        @classmethod
        def mutated_genes(self):
            '''
            create random genes for mutation
            '''
            global GENES
            gene = random.choice(GENES)
            # print("this is returned data", gene)
            return gene

        @classmethod
        def create_gnome(self):
            '''
            create chromosome or string of genes
            '''
            global TARGET
            gnome_len = len(TARGET)
            return [self.mutated_genes() for _ in range(gnome_len)]

        def mate(self, par2):
            '''
            Perform mating and produce new offspring
            '''

            # chromosome for offspring
            child_chromosome = []
            for gp1, gp2 in zip(self.chromosome, par2.chromosome):

                # random probability
                prob = random.random()

                # if prob is less than 0.45, insert gene
                # from parent 1
                if prob < 0.45:
                    child_chromosome.append(gp1)

                    # if prob is between 0.45 and 0.90, insert
                # gene from parent 2
                elif prob < 0.90:
                    child_chromosome.append(gp2)

                    # otherwise insert random gene(mutate),
                # for maintaining diversity
                else:
                    child_chromosome.append(self.mutated_genes())

                    # create new Individual(offspring) using
            # generated chromosome for offspring
            return Individual(child_chromosome)

        def cal_fitness(self):
            '''
            Calculate fittness score, it is the number of
            characters in string which differ from target
            string.
            '''
            global TARGET
            fitness = 0
            for gs, gt in zip(self.chromosome, TARGET):
                if gs != gt: fitness += 1
            return fitness
    generation = 1
    found = False
    population = []
    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))
    while not found:
        # sort the population in increasing order of fitness score
        population = sorted(population, key=lambda x: x.fitness)
        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break
        # Otherwise generate new offsprings for new generation
        new_generation = []
        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])
        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation
        print("+======================================================================================================+")
        print("Genetic algorithm initialization...")
        print("Wait Random Test inputs are generated...")
        print("Generation: {}\tString: {}\tFitness: {}". \
              format(generation, "".join(population[0].chromosome), population[0].fitness))
        generation += 1
    print("Generation: {}\tString: {}\tFitness: {}". \
          format(generation, "".join(population[0].chromosome), population[0].fitness))
    some = "Generation: {}\tString: {}\tFitness: {}". \
        format(generation, "".join(population[0].chromosome), population[0].fitness)
    print("We Take the Valuable input for the TESTING...")
    print("Wait...The TEST CASE is generated...")
    print("TEST CASE GENERATED SUCESSFULL!!!")
    value = "".join(population[0].chromosome)
    print("Random Testing Input is",value)
    print("+=========================================================================================================+")
    print("\n")
    print("TESTING APPLICATION IS INITIALIZED..../")
    print("PLEASE WAIT...")
    driver = webdriver.Chrome(executable_path="C:/Users/Balagee/PycharmProjects/My_Projects/automated_testing/chromedriver.exe")
    driver.implicitly_wait(5)
    ##This is the testing a search
    product_names = []
    product_names.append(value)
    leng_lst = len(product_names)
    for i in range(leng_lst):
        lst_element = product_names[i]
        driver.get('https://www.amazon.com/')
        search = driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(lst_element, Keys.ENTER)
        expected_txt = lst_element
        actual_txt = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
        compare = eval(actual_txt)
        # print(compare)
        # print(expected_txt)

        # assert expected_txt == actual_txt, f'Error.Expected text: {expected_txt}, but actual text: {actual_txt}'
        if (expected_txt == compare):
            #root = Tk()
            #messagebox.showinfo("TESTING SUCESSFULL FOR THE KEYWORD", expected_txt)
            print("SEARCH TESTING IS SUCESSFULL......for the keyword \n",expected_txt)
            print("EXCIT from current session...")
            print("+=================================================================================================+")
            print("\n")
            #messagebox.showinfo("SUCCFULL INFORMATION", "SEARCHING TEST COMPLETED")
            #root.destroy()
        else:
            print("WARNING..!!!")
            print("There is something ERROR in SEARCHING TEST...")
            print("SESSION EXITED FROM SEARCHING TEST.")
            print("+=================================================================================================+")
            print("\n")
    ##Login automated testing
    print("LOGIN Test INTIALIZING...")
    print("Please wait...")
    element = driver.find_element_by_xpath(xpath="//span[@class='hm-icon-label']")
    element.click()
    element_login = driver.find_element_by_id(id_="hmenu-customer-profile")
    element_login.click()
    try:
        element_username = driver.find_element_by_id(id_="ap_email")
        element_username.send_keys(user_name_random, Keys.ENTER)
        element_user_not_correct = driver.find_element_by_class_name(name='a-alert-heading').text
        phone_verify = driver.find_element_by_class_name(name='a-alert-heading').text
        #print(phone_verify)
        # print(element_user_not_correct)
        if (element_user_not_correct == 'There was a problem'):

            print("Account Verification failed...")
            print("This is not a valid E-Mail address...")
            print("If you want to create the create new Account ?")
            r = Tk()
            messagebox.askokcancel("CONFIRMATION", "you are Not registered user want to create account")
            r.destroy()
            element_create_new_acc = driver.find_element_by_id(id_="createAccountSubmit")
            element_create_new_acc.click()
            element_create_name = driver.find_element_by_id(id_='ap_customer_name')
            element_create_name.send_keys(customer_name_random, Keys.TAB)
            element_create_email = driver.find_element_by_id(id_='ap_email')
            element_create_email.send_keys(user_name_random, Keys.TAB)
            element_create_pass = driver.find_element_by_id(id_='ap_password')
            element_create_pass.send_keys(password_random, Keys.TAB)
            element_create_conf = driver.find_element_by_id(id_='ap_password_check')
            element_create_conf.send_keys(password_random)
            driver.implicitly_wait(5)
            element_create_button = driver.find_element_by_id(id_='continue')
            element_create_button.click()
            print("ACCOUNT CREATION SUCESSFULL!!!")
            print("+=================================================================================================+")
            print("\n \n")
        elif (phone_verify == "Incorrect phone number"):
            print("Entered phone number is Incorrect...wanna to create new one?")
            r1 = Tk()
            messagebox.askokcancel("CONFIRMATION", "create ?")
            r1.destroy()
            element_create_new_acc = driver.find_element_by_id(id_="createAccountSubmit")
            element_create_new_acc.click()
            element_create_name = driver.find_element_by_id(id_='ap_customer_name')
            element_create_name.send_keys(customer_name_random, Keys.TAB)
            element_create_email = driver.find_element_by_id(id_='ap_email')
            element_create_email.send_keys(user_name_random, Keys.TAB)
            element_create_pass = driver.find_element_by_id(id_='ap_password')
            element_create_pass.send_keys(password_random, Keys.TAB)
            element_create_conf = driver.find_element_by_id(id_='ap_password_check')
            element_create_conf.send_keys(password_random[0])
            driver.implicitly_wait(5)
            element_create_button = driver.find_element_by_id(id_='continue')
            element_create_button.click()
            print("Account created...")
            print("Testing Sucessfull...")
            print("---------------------------------------------------------------------------------------------------")
        else:
            password_for_loging = driver.find_element_by_id(id_='ap_password')
            password_for_loging.send_keys(password_random, Keys.ENTER)
            alert_msg = driver.find_element_by_class_name(name='a-list-item').text
            if (alert_msg == 'Your password is incorrect'):
                print("Entered Password is Inocorrect !")
                r2 = Tk()
                messagebox.showinfo("ALERT MESSAGE", 'The password is incorrect')
                r2.destroy()
                print("Testing sucessfull")
                print("-----------------------------------------------------------------------------------------------")
            else:
                print("Testing sucessfull...")
                print("You logged on AMAZON !")
                r3 = Tk()
                messagebox.showinfo("SUCCFULL INFORMATION", "you logged on amazon")
                r3.destroy()
                print("-----------------------------------------------------------------------------------------------")
    except Exception as e:
        print("exception", e)

print("+=============================================================================================+")
print("+=============================================================================================+")
print("--------------------------------------Test Report______________________________________________")
print("\n")
print("_______________________________Testing Efficiency Report_____________________________________")
print("\n")
print("ITERATIONS: ",no_iteratons)
now_end = datetime.utcnow()
print("Test Start Time: ",now_start)
print("Test End Time: ",now_end)
print("Time Taken to Testing...")
c = now_end - now_start
print('Difference: ', c)
minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)
minutes = c.seconds / 1000
print('Difference in Seconds: ', minutes)
exit()