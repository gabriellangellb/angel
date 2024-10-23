#A little about myself
names = "Gabriella Angel Bayinze Lukyamuzi."
dob = "10/01/2004.";
gender = "Female";
nationality = "Ugandan.";
hobbies = "Swimming,Travelling, Shopping, Watching movies, Family time,Friends.";

print (f"My name is {names} I was born on {dob} I am a {gender} {nationality} I love {hobbies}");


#simple function
try:
    base = 5
    height = 10
    area = (0.5 *base* height)
    print(f" Area: {area}")
except (ValueError, TypeError) as e:
    print(e)

