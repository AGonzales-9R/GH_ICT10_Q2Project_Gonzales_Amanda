from pyscript import display, document

def gleeClub(e):
    document.getElementById('clubInfo').innerHTML= " "

    glee_club = {
        'Name':'Glee Club',
        'Description':'Love to sing? Love to perform? Glee Club is the place for you!',
        'Meeting time':'Monday and Thursday, 3PM-4:30PM',
        'Location':'Music Room',
        'Club moderator':'Ms. Loyola',
        'Number of members':'30'
    }
    
    glee = f"""

    {glee_club['Name']}
    Description: {glee_club['Description']}   
    Meeting time: {glee_club['Meeting time']}
    Location: {glee_club['Location']}
    Club moderator: {glee_club['Club moderator']}
    Number of members: {glee_club['Number of members']}

    """

    display(glee, target='clubInfo')


def danceClub(e):
    document.getElementById('clubInfo').innerHTML= " "

    dance_club = {
        'Name':'Dance Club/Monarchs',
        'Description':'Dance Club is a fun, energetic community where anyone can express themselves through movement!',
        'Meeting time':'Monday and Thursday, 3PM-5PM',
        'Location':'Room 501-502',
        'Club moderator':'Mr. Marutani',
        'Number of members':'12'
    }
    
    dance = f"""

    {dance_club['Name']}
    Description: {dance_club['Description']}   
    Meeting time: {dance_club['Meeting time']}
    Location: {dance_club['Location']}
    Club moderator: {dance_club['Club moderator']}
    Number of members: {dance_club['Number of members']}

    """

    display(dance, target='clubInfo')


def commArts(e):
    document.getElementById('clubInfo').innerHTML= " "

    comm_arts = {
        'Name':'Communication Arts Club',
        'Description':'The Communication Arts Club is a space where students can explore through writing, speech, and media!',
        'Meeting time':'Monday: 2:30PM-3:30PM, Tuesday: 2:30PM-4:30PM',
        'Location':'Room 711',
        'Club moderator':'Mr. Loreto',
        'Number of members':'20'
    }
    
    commarts = f"""

    {comm_arts['Name']}
    Description: {comm_arts['Description']}   
    Meeting time: {comm_arts['Meeting time']}
    Location: {comm_arts['Location']}
    Club moderator: {comm_arts['Club moderator']}
    Number of members: {comm_arts['Number of members']}

    """

    display(commarts, target='clubInfo')

def artClub(e):
    document.getElementById('clubInfo').innerHTML= " "

    art_club = {
        'Name':'Art Club',
        'Description':'Love to draw? Paint? Build? Create cool things? Art Club is your creative playground!',
        'Meeting time':'Tuesday and Thursday, 3PM-4PM',
        'Location':'Event Room',
        'Club moderator':'Ms. Suarez',
        'Number of members':'30'
    }
    
    art = f"""

    {art_club['Name']}
    Description: {art_club['Description']}   
    Meeting time: {art_club['Meeting time']}
    Location: {art_club['Location']}
    Club moderator: {art_club['Club moderator']}
    Number of members: {art_club['Number of members']}

    """

    display(art, target='clubInfo')    