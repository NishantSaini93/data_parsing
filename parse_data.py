import operator
import json
class ParseDataMoviesActors:
    """
    Class to parse the data from movies data.json file
    """
    def __init__(self):
        #Instance variable to store the data loaded from data.json file
        self.__data_from_file=[]
        ##Dictionary to save the parsed data we need for output
        self.__output_data={}

    def loadFile(self):
        """
        Function to load the data.json file
        """
        try:
            file=open("data.json","r")
            self.__data_from_file = json.load(file)
        except Exception as error:
            print("No file or data found {}".format(error))
            return False
        return True

    def parseData(self):
        """
        FUnction to parse the data loaded from data.json
        """

        #loop to go over every movie present in the data.json
        for movies in self.__data_from_file:
            actorlist=movies["stars"].split(",")

            #Extract the actorw name related to movie
            for actor in actorlist:
                actor_name=actor.lstrip()
                #Adding the formatting so we can produce needed output
                actor_name="\'"+actor_name+"\'"

                #Checking if the actor is already present in the dictionary or not because we need to add the
                # if not present otherwise update the details if already exist
                movies_details=self.__output_data.get(actor_name,None)
                try:
                    if movies_details is None:
                        self.__output_data[actor_name]=[1,float(movies["rating"])]
                    else:
                        self.__output_data[actor_name][0]=movies_details[0]+1
                        self.__output_data[actor_name][1]=movies_details[1]+float(movies["rating"])
                except Exception as error:
                    print("Unable to use data of entry {} because {}".format(movies,error))
        return True

    def display(self):
        """
        Function to display out put
        """

        ##logic to sort the data as we need sorted output
        sorted_data = dict( sorted(self.__output_data.items(), key=operator.itemgetter(1)))

        ##Logic to print the data
        for element in sorted_data:
            #if the count of movies is less than 2 dont do anything
            if sorted_data[element][0]<2:
                continue
            else:
                avg=sorted_data[element][1]/sorted_data[element][0]
                print("Star Name: {0:<20}|Movies: {1} | AVG Rating: {2:0.2f}".format(element,sorted_data[element][0],avg))
        return True

if __name__ == "__main__":
    object_of_data_class=ParseDataMoviesActors()
    result1=object_of_data_class.loadFile()
    if result1==False:
        print("Unable to load data existing")
    else:
        result2=object_of_data_class.parseData()
        result3=object_of_data_class.display()
        if result2 and result3:
            pass
        else:
            print("Parsing failed")















