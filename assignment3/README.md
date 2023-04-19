# Homework 3: Log Bird Sightings

In this assignment, you will create an app that enables you to log sightings of birds. 

You should create a table with the following fields: 

- "bird"
- "weight"
- "diet"
- "habitat" (these four fields are as in the json file),
- "n_sightings" (an integer)
- "user_email" (of the user who saw it)

The user_email is used to let users see only their own sightings by default. 

If you want to add validation, you can use `requires=validator`, see the documentation for form validation.

When a user goes to the /index page, they should see a table for their own sightings.  Assuming that you call the table `bird`, you can obtain this via 

    db(db.bird.user_email == get_user_email()).select()
    
(see the chapter on the database for more commands you can use).  The table should have the following columns: 

- `bird`
- `weight`
- `diet`
- `habitat`
- `n_sightings`
- a button to edit the entry (similarly to what done in the last video of Unit 8). 
- a `+1` button to increment by 1 the sightings count.  The button should be a signed URL (similarly to what done in the last video of Unit 8 for deletion.)

On top of the table, there should be a button [+] for adding a new entry.  Again, the last video of Unit 8 shows you essentially how to do all of this. 
Thus, you will need the following controllers: 

- `index` : to display the table
- `add` : to add a new entry. 
- `edit<id>` : to edit an entry.  Check that the entry belongs to the user editing it!  Do not let a user edit entries belonging to other users! 
- `inc/<id>` : to increment the count of an entry. 

You should use the starting code homework3_starter. 
The /inc action, as mentioned, should be implemented as a signed URL.  In practice you will define the controller like (see the delete controller in Unit 8): 

    @action('/inc/<bird_id:int>')
    @action.uses(db, auth)
    def inc(bird_id):
       ...

The `edit` action should check that only the user to whom the row belongs (the user whose email is in the row) can edit it.  You can achieve this by either signing the `edit` URL, or by checking in the edit controller that the user who is logged in is the user to whom the row belongs. Your choice.
