def finalposition(move):
                l=len(move)
                cR=0                            #RIGHT COUNTER
                cL=0                            #LEFT COUNTER
                cU=0                            #UP COUNTER
                cD=0                            #DOWN COUNTER

                for i in range(l):
                                if(move[i]=='U'):
                                                cU+=1
                                elif(move[i]=='D'):
                                                cD+=1
                                elif(move[i]=='R'):
                                                cR+=1
                                elif(move[i]=='L'):
                                                cL+=1

                coordinate1= cR-cL
                coordinate2= cU-cD

                if(coordinate1==0 and coordinate2==0):
                                return True
                else:
                                return False


move="UD"
finalposition(move)

