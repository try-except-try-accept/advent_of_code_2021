


with open("day4.txt") as f:


     with open("day4new.txt", "w") as f2:


          lines = f.readlines()


          for line in lines:

               if line.strip() == "":
                    line = "x\n"

               f2.write(line)
