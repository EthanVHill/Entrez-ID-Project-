# Loading JSON file
# https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html
# Example:
# import json
#
# # Reading data back
# with open('data.json', 'r') as f:
#      data = json.load(f)

import json

# From Table S13 in Plaisier et al., Cell Systems 2016
input = ['430', '1052', '1053', '1385', '84699', '9586', '1871', '1874', '144455', '79733', '1960', '1997', '2002', '2004', '80712', '2114', '2115', '2120', '51513', '2551', '2623', '2624', '2625', '9421', '3232', '10320', '3659', '3662', '3670', '91464', '3726', '10661', '11278', '128209', '10365', '9314', '1316', '51176', '9935', '23269', '4602', '4774', '4790', '7025', '9480', '5468', '5914', '5916', '3516', '5971', '864', '6257', '4093', '6659', '6660', '6662', '25803', '347853', '30009', '9496', '6929', '6925', '8463', '7022', '29842', '10155', '6935', '132625', '23051', '85416', '7707', '7764', '23528', '201516']

# Reading data back
tfbsDb = {}
with open('tfbsDb_plus_and_minus_5000_entrez.json', 'r') as f:
     tfbsDb = json.load(f)

# Sample of keys in tfbsDb
print(list(tfbsDb.keys())[0:5])

# Sample of values
print(tfbsDb[list(tfbsDb.keys())[0]][0:5])


with open('tfbsDb_plus_and_minus_5000_entrez.json', 'r') as f:
    data  =  json.load(f)

translator = {}    
with open('id_conversion/humanTFs_All.csv', 'r' ) as d:
    d.readline() #get rid of header
    while 1:
        inline = d.readline() 
        if not inline: 
            break 
        splitup = inline.strip().split(',')
        if not splitup[2] in translator:
            translator[splitup[2]] = []
        translator[splitup[2]].append(splitup[0])

families = []
with open('id_conversion/tfFamilies.csv', 'r' ) as e:
    e.readline() 
    while 1:
        inline2 = e.readline() 
        if not inline2: 
            break 
        families.append(inline2.strip().split(',')[2].split(' '))

# Main code
tfNetwork = {}
input2 = []        
for tfReg in input: #tfReg is a single entrez id from input 
    tfTarg = [] 
    if tfReg in translator:    #if our ingle inout is in trnaslator
        for mot1 in translator[tfReg]: #mot1 is now the output of the translator 
            #uzing the input(tfTReg) as Keys, should output motif names and store in mot1
            if mot1 in data:   #if mot1(Motifnames) are in data
                tmp = data[mot1]   #tmp is now the entrez ID's outputted by the data using mot1 as its key
                for i in tmp: # Variable i is now tmp
                    if i in input and not i in tfTarg:   #IF i is in input and not already in tfTarg, make an appendix tfTarg
                        tfTarg.append(i)
    else:
        input2.append(tfReg)  #input2 is a single number
        for tfReg in input2: # tfReg is a single value from the list of entrez id's in input2
            for familyMembers in families: #familyMember is a single list of family entrez Id's
                if tfReg in familyMembers: #if our single entrez matches any of the entrez in the single list of familyMember, output list
                        for tfReg in familyMembers:  #tfReg is now a single entrez ID from the single entrezList
                            tfTarg = [] #Empty list
                            if tfReg in translator: #if our single entrez id is in translator
                                for mot2 in translator[tfReg]:#mot 2 is is a motif with our single entrez id(tfReg) being the key
                                    if mot2 in data:  
                                        tmp2 = data[mot2] 
                                        for l in tmp2:
                                            if l in familyMembers and not l in tfTarg:  
                                                tfTarg.append(l)
                                            
                            else:
                                print('No motif final '+tfReg)
                            tfNetwork[tfReg] = tfTarg

           
#tfFamilyNetwork = []        
#for tfReg in input2:
#    for familyMembers in families:
#        if tfReg in familyMembers:
#            print(familyMembers)



#            from itertools import chain 
#            flattened = list(chain.from_iterable(leftOver))

#            flattened = []
#            for sublist in leftOver:
#                for mot3 in sublist:
#                    flattened.append(mot3)
                    # final bit would be transferring the list of lists into a list
#                    
#flattened =['10488', '90993', '64764', '84699', '148327', '7291', '117581', 
#            '9421', '9464', '6939', '100129885', '256297', '344018', '3725', 
#            '3726', '3727', '10661', '7071', '8462', '11278', '51621', 
#            '136259', '28999', '83855', '128209', '10365', '51274', '9314', 
#            '688', '1316', '8609', '11279', '687', '5970', '5971', '5966', 
#            '4086', '4087', '4088', '4090', '4093', '6899', '347853', '6913', 
#            '9096', '57057', '50945', '11244', '22882', '23051', '57594', 
#            '360030', '2735', '84107', '85416', '2736', '2737', '148979', 
#            '84662', '169792', '7545', '7546', '7547']         
#print('\n')
#tfNetworkPart2 = {}
#for tfRegP2 in flattened: 
#    tfTargP2 = [] 
#    if tfRegP2 in translator:    
#        for mot4 in translator[tfRegP2]: 
#            if mot4 in data:  
#                tmp2 = data[mot4] 
#                for l in tmp2:
#                    if l in flattened and not l in tfTargP2:  
#                        tfTargP2.append(l)
#    else:
#        print('No motif final '+tfRegP2)
#    tfNetworkPart2[tfRegP2] = tfTargP2