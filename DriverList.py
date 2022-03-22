import xml.etree.ElementTree as ET
import requests

from typing import List

class APIConnection():
    
    r : any 
    
    def __init__(self, year : int, race : int, event : str):
        
        url = f"http://ergast.com/api/f1/{str(year)}/{str(race)}/{event}"

        payload={}
        headers = {}

        self.r = requests.request("GET", url, headers=headers, data=payload)
        
class DriverList(APIConnection):
    
    year : int
    race : int
    event : str
    
    url : str
    tree : any
    root : any
    
    def __init__(self : any, year : int, race : int, event : str) -> None:
        super().__init__(year, race, event)
        
        self.year = year
        self.race = race
        self.event = event
        
    def _generate_tree(self):
        
        tree =  ET.ElementTree(ET.fromstring(self.r.content))
        self.root = tree.getroot()

    @staticmethod
    def _return_key(key : str) -> str:
        d_url = "{http://ergast.com/mrd/1.5}"     
        return d_url + key

    def get_result(self : any) -> List[str]:
        
        self._generate_tree() # Generating Tree Element
                    
        result_result = {}
            
        for result in self.root[0][0][4]: 
            
            try: 
                if self.event == "qualifying":        
                    result_result[result.get("position")] = {"Driver" : f"{result[0][1].text} {result[0][2].text}",
                                                            "Constructor" : result[1][0].text,
                                                            "Q1" : result[2].text if len(result) >= 3 else None,
                                                            "Q2" : result[3].text if len(result) >= 4 else None,
                                                            "Q3" : result[4].text if len(result) >= 5 else None}
                
                if self.event == "results":        
                    result_result[result.get("position")] = {"Driver" : f"{result[0][1].text} {result[0][2].text}",
                                                            "Constructor" : result[1][0].text}
            
            except IndexError:
                result_result[result.get("position")] = {"Driver" : f"{result[0][1].text} {result[0][2].text}"}
                                                                                     
        return result_result
    
def main():
    
    #driver_list = DriverList(2022, 1, "qualifying")
    driver_list = DriverList(2022, 1, "results")

    print(driver_list.get_result())
  
if __name__ == "__main__":
    main()
    








# print(root)