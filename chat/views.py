from django.shortcuts import render, redirect
from .models import Room, Message    # To access our database to use for our views
from django.http import HttpResponse, JsonResponse 


# Create your views here.
def index(request):
    return render(request,'index.html')

def room(request, room):     #Collecting room variable passed in its dynamic url
    username = request.GET.get('username')   #getting it by url from the html
    room_details = Room.objects.get(name=room)   #getting the name of the room through the model object
    return render(request, 'room.html',{
        'username': username,
        'room_details': room_details,
        'room': room,
    })  # To send this dictionary data(username and room_details) to our html template


def assessview(request):    #To check existence of a room before function 
    if request.method == 'POST':
        room = request.POST['room_name']   
        username = request.POST['username']

    if Room.objects.filter(name=room).exists():     #If an existing "room" correlates with the "name" of room inputted by a certain user
        return redirect('/' +room+'/?username=' +username)  #take user to the room with the name
        
    
    else:
        new_room = Room.objects.create(name=room)    #if not existing, Create a "room" name correlating with the "name" inputted by user
        new_room.save()
        return redirect('/' +room+'/?username=' +username)   #take user to the room with the name


def send(request):   #To access the data ajax sent to the url
    message = request.POST['message']
    username = request.POST['username']       #We are getting the data and passing it to a variable
    room_id = request.POST['room_id']

    new_message = Message.objects.create(user=username, value=message, room=room_id)      #Create an object with our variables
    new_message.save() 
    return HttpResponse('Message Sent')    #Is our Alert data passing to Ajax


def getMessages(request, room):     #To get messages in a particular room to be displayed, we collected the room variable to access it
    room_details = Room.objects.get(name=room)     #getting the name of the room through the model object

    messages = Message.objects.filter(room=room_details.id) #To filter from all to get only the room that correlates with our variable above(ROOM NAME) .id(ROOM)
    return JsonResponse({"messages":list(messages.values())})   #To return in json as a variable of "messages" assigned to a list of messages holding all these values


