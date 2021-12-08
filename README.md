# Dialogue-System-for-games
| NOT COMPLETE |

Both the xml and json files use a npc id and a conversation id, which mean that conversations that previously happend can be accounted for and based on different
situations the dialogue output can be dynamically changed:

Example (For the same conversation):

If they player has done something that could have angered the NPC he might use conversation id 2 instead of 1 in order to show this in the dialogue, but also give the player the same conversation. 

What I would change:

Maybe instead of storing the conversation in the conversation id conatainer , have a pointer , pointing to another file , or its address in memory . This could also mean that the text can be compressed and it wouldn't have to follow the protocals of a markup language 
