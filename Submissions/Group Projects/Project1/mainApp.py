## Menu
def menu():
  # Printing Menu
  print("\nMain Menu:")
  print("""----------
        \n1. Add a Visited URL  \n2. Delete a Visited URL  \n3. View Your Browsing History \n4. Track a Visited URL \n5. Format Browsing History \n6. History Backup \n7. Restore History Backup  \n8. Total Tracked URLs \n
        \n** Any other key to exit!!\n
        """)
  return input("Enter your choice: ")
  
  
  ## Driver method
  
  if __name__ == "__main__":

  ## Showing Menu
  thisTracker = historyTracker()

  while (True): 
    clear_output()
    choice = menu()
    
    ## Decision
    if choice == '1':
      # Add a Visited URL
      clear_output(wait=True) 
      flag = thisTracker.insert()
      tempChoice = 'y'
      while flag and (tempChoice == 'y' or tempChoice == 'Y'):
        clear_output(wait=True) 
        tempChoice = input("\nWanna add another URL? (Y/N): ")
        if tempChoice == 'y' or tempChoice == 'Y':
          flag = thisTracker.insert()
        else:
          break
      if not flag:
        input("\nPress Enter!!")
      
    
    elif choice == '2':
      # Delete a Visited URL
      clear_output(wait=True) 
      flag = thisTracker.delete()
      tempChoice = 'y'
      while flag and (tempChoice == 'y' or tempChoice == 'Y'):
        clear_output(wait=True) 
        tempChoice = input("\nWanna delete another history? (Y/N): ")
        if tempChoice == 'y' or tempChoice == 'Y':
          flag = thisTracker.delete()
        else:
          break
      if not flag:
        input("\nPress Enter!!")
    
    elif choice == '3':
      # Show Complete Browsing History
      clear_output(wait=True) 
      thisTracker.historyViewer()
      input("\nPress Enter!!")  
    
    elif choice == '4':
      # Find a Visited URL
      clear_output(wait=True) 
      flag = thisTracker.search()
      tempChoice = 'y'
      while flag and (tempChoice == 'y' or tempChoice == 'Y'):
        clear_output(wait=True) 
        tempChoice = input("\nWanna track history again? (Y/N): ")
        if tempChoice == 'y' or tempChoice == 'Y':
          flag = thisTracker.search()
        else:
          break
      if not flag:
        input("\nPress Enter!!") 
    
    elif choice == '5':
      # Format Browsing History
      clear_output(wait=True) 
      thisTracker.refreshMemory()
      input("\nPress Enter!!")  
    
    elif choice == '6':
      # Backup Browsing History
      clear_output(wait=True) 
      thisTracker.backupHistory()
      input("\nPress Enter!!")  
    
    elif choice == '7':
      # Restore Browsing History
      clear_output(wait=True)
      thisTracker.restoreBackup()
      input("\nPress Enter!!")  
    
    elif choice == '8':
      # Total Tracked URLs
      clear_output(wait=True)
      thisTracker.countHistory()
      input("\nPress Enter!!")
    
    else:
      del(thisTracker)
      clear_output()
      print("\nGood Bye!!")
      break
  

  
