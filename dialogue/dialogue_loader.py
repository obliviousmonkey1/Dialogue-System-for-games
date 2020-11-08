import json
import xml.etree.ElementTree as ET

npc_current_id = "0"
npc_current_conversation_id = "0"
npc_current_state_id = "1"

dialogue_bool = True

class dialogue_structure():
    def __init__(self, player_response_file, root, npc_id,npc_current_conversation_id, npc_current_state_id, dialogue_bool):
        self.player_response_file = player_response_file
        self.root = root
        self.npc_id = npc_id
        self.npc_current_conversation_id = npc_current_conversation_id
        self.npc_current_state_id = npc_current_state_id
        self.npc_dialogue_holder : list[str] = []
        self.player_response_holder : list[str] = []
        self.dialogue_bool = dialogue_bool
        
    def consumer(self):
        for i in self.root[int(self.npc_id)][int(self.npc_current_conversation_id)]:
            if i.attrib["state_id"] == self.npc_current_state_id:
                for p in range(len(i)):
                    self.npc_dialogue_holder.append(i[p].text)
        

    def producer(self):
        a = 1
        if self.player_response_file[self.npc_id][self.npc_current_conversation_id][self.npc_current_state_id]["type"] == "response":
            for i in self.player_response_file[self.npc_id][self.npc_current_conversation_id][self.npc_current_state_id]:
                if "text" in i:
                    self.player_response_holder.append(" {} : {}".format(a, self.player_response_file[self.npc_id][self.npc_current_conversation_id][self.npc_current_state_id][i][0]))
                    a +=1
        elif self.player_response_file[self.npc_id][self.npc_current_conversation_id][self.npc_current_state_id]["type"] == "FALSE":
            self.player_response_holder.append(False)

        
    def display(self):
        for i in range(len(self.npc_dialogue_holder)):
            print(self.npc_dialogue_holder[i])
            if i+1 != len(self.npc_dialogue_holder):
                dialogue_pause = input("<continue> ")
            else:
                if False in  self.player_response_holder:
                    return self.dialogue_bool == False , self.npc_current_state_id
                
                for p in self.player_response_holder:
                    print(p)
                player_choice = str(input("> "))

        if self.player_response_file[self.npc_id][self.npc_current_conversation_id][self.npc_current_state_id]["text" + player_choice][1] == "FALSE":
            return self.dialogue_bool == False , self.npc_current_state_id

        self.npc_current_state_id = self.player_response_file[self.npc_id][self.npc_current_conversation_id][self.npc_current_state_id]["text" + player_choice][1]
        return self.dialogue_bool, self.npc_current_state_id


## loaders are for testing ##

# .json loader
with open("player_response.json", "r") as f:
    player_response_file = json.load(f)

# .xml loader
tree = ET.parse("npc_dialogue.xml")
root = tree.getroot()


if __name__ == "__main__":

    while dialogue_bool == True:    
        s = dialogue_structure(player_response_file, root, npc_current_id, npc_current_conversation_id, npc_current_state_id, dialogue_bool)
        s.consumer()
        s.producer()
        dialogue_bool, npc_current_state_id = s.display()
