import hashlib #SHA256

def hashgenerator(data): 
  result= hashlib.sha256(data.encode())
  return result.hexdigest()

class Block: #creating block
  def __init__(self,data,hash,prev_hash):
    self.data=data #importing data 
    self.hash=hash #importinh hash
    self.prev_hash=prev_hash#importing prev_hash
    
class Blockain:
  def __init__(self):
    hashlast= hashgenerator('abcd')
    hashstart= hashgenerator('efgh')
                    #(data,  hash ,   prev_hash)
    genesis= Block('ijkl',hashstart,hashlast) #1st block 
    self.chain=[genesis] # making genesis a part of blockchain

  def add_block(self,data):
     prev_hash=self.chain[-1].hash  #it stores the hash of the last block present on the chain
     hash= hashgenerator(data+prev_hash)
     block= Block(data,hash,prev_hash)
     self.chain.append(block)

bc=Blockain()
bc.add_block("123")
bc.add_block("456")
bc.add_block("789")

for block in bc.chain:
  print(block.__dict__)
    

  