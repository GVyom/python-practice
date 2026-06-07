enemies = 1 #<- this is global scope variable

def increase_enemies():
    enemies = 5
    print(f"Number of enemies: {enemies}")

increase_enemies()
print(f"Number of enemies outside the function: {enemies}")

#This happened due to scope. The variable 'enemies' inside the function is a local variable, and it does not affect the global variable 'enemies' outside the function. To modify the global variable, you can use the 'global' keyword:   
# Local Scope
def drink_portion():
    global portion_size #global allowed it to make it from local to global for every function
    portion_size = 100
    print(f"Portion size: {portion_size}ml") 

drink_portion()
print(portion_size)  # This will raise an error because portion_size is not defined in the global scope.    

#global Scope: Always use Capital letters for global variables to avoid confusion with local variables.