def data(user_name, used_data, limit_data):

    data_monitoring = limit_data - used_data

    print("User = " , user_name)
    print("Data  Used = " , used_data)
    print("Data left = " , data_monitoring )

    if data_monitoring <= 0:
        message = "Data is going to expire"

    elif data_monitoring <= 0.5 :
        message = "You left 50% Data"

    else :
        message = " You have a Data You can use"

    print("SMS message: " ,message)

data( "Rahul ", 1.5,2.0)
data("Roshani", 2.0,2.0)
data("Monu", 2.0,3.0)
