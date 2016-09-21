#import requests library
import requests

#import json library
import json

# Disable warnings
requests.packages.urllib3.disable_warnings()

#controller='sandboxapic.cisco.com'
controller='devnetapi.cisco.com/sandbox/apic_em'


def getTicket():
    # put the ip address or dns of your apic-em controller in this url
    url = "https://" + controller + "/api/v1/ticket"

    #the username and password to access the APIC-EM Controller
    payload = {"username":"devnetuser","password":"Cisco123!"}

    #Content type must be included in the header
    header = {"content-type": "application/json"}

    #Performs a POST on the specified url to get the service ticket
    response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

    print (response)

    #convert response to json format
    r_json=response.json()

    #parse the json to get the service ticket
    ticket = r_json["response"]["serviceTicket"]

    return ticket



def getTopology(ticket):
    # URL for topology REST API call to get list of existing devices on the network, and build topology
    url = "https://" + controller + "/api/v1/topology/physical-topology"

    #Content type as well as the ticket must be included in the header
    header = {"content-type": "application/json", "X-Auth-Token":ticket}

    # this statement performs a GET on the specified network device url
    response = requests.get(url, headers=header, verify=False)

    # json.dumps serializes the json into a string and allows us to
    # print the response in a 'pretty' format with indentation etc.
    print ("Topology = ")
    print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

    #convert data to json format.
    r_json=response.json()

    #Iterate through network device data and list the nodes, their interfaces, status and to what they connect
    for n in r_json["response"]["nodes"]:        
        print()
        print()
        print('{:30}'.format("Node") + '{:25}'.format("Family") + '{:20}'.format("Label")+ "Management IP")
        if "platformId" in n:
            print('{:30}'.format(n["platformId"]) + '{:25}'.format(n["family"]) + '{:20.14}'.format(n["label"]) + n["ip"])
        else:
            print('{:30}'.format(n["role"]) + '{:25}'.format(n["family"]) + '{:20.14}'.format(n["label"]) + n["ip"])
        found=0    #print header flag
        printed=0  #formatting flag
        for i in r_json["response"]["links"]:
            #check that the source device id for the interface matches the node id.  Means interface originated from this device.
            if i["source"] == n["id"]:
                if found==0:
                    print('{:>20}'.format("Source Interface") + '{:>15}'.format("Target") +'{:>28}'.format("Target Interface") + '{:>15}'.format("Status") )
                    found=1
                    printed=1                    
                for n1 in r_json["response"]["nodes"]:
                    #find name of node to which this one connects
                    if i["target"] == n1["id"]:
                        if "startPortName" in i:
                            print("    " + '{:<25}'.format(i["startPortName"]) + '{:<18.14}'.format(n1["label"]) + '{:<25}'.format(i["endPortName"]) + '{:<9}'.format(i["linkStatus"]) )
                        else:
                            print("    " + '{:<25}'.format("unknown") + '{:<18.14}'.format(n1["label"]) + '{:<25}'.format("unknown") + '{:<9}'.format(i["linkStatus"]) )
                        break;
        found=0                
        for i in r_json["response"]["links"]:
            #Find interfaces that link to this one which means this node is the target.
            if i["target"] == n["id"]:
                if found==0:
                    if printed==1:
                        print()
                    print('{:>10}'.format("Source") + '{:>30}'.format("Source Interface") + '{:>25}'.format("Target Interface") + '{:>13}'.format("Status"))
                    found=1                    
                for n1 in r_json["response"]["nodes"]:
                    #find name of node to that connects to this one
                    if i["source"] == n1["id"]:
                        if "startPortName" in i:                            
                            print("    " + '{:<20}'.format(n1["label"]) + '{:<25}'.format(i["startPortName"]) + '{:<23}'.format(i["endPortName"]) + '{:<8}'.format(i["linkStatus"]))
                        else:
                            print("    " + '{:<20}'.format(n1["label"]) + '{:<25}'.format("unknown") + '{:<23}'.format("unknown") + '{:<8}'.format(i["linkStatus"]))
                        break;

theTicket=getTicket()
getTopology(theTicket)

