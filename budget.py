import itertools

class Category:
  def __init__(self, name=""):
    self.name = name
    self.balance = 0
    self.ledger = []

  def __str__(self):
    title = "{:*^30}".format(self.name)
    lines = ""
    for i in self.ledger:
      lines += "{description:<23.23s}{amount:>7.2f}\n".format(**i, width = 30)

    return f"{title}\n{lines}Total: {self.balance:.2f}"

  def deposit(self, amount, description=""):
    self.balance += amount
    deposit = {"amount": amount, "description": description}
    self.ledger.append(deposit)


  def withdraw(self, amount, description=""):
    if self.check_funds(amount) is True:
      self.balance += -amount
      withdrawal = {"amount": -amount, "description": description}
      self.ledger.append(withdrawal)
      return True
    else:
      return False

  def get_balance(self):
    return round(self.balance, 2)

  def transfer(self, amount, category):
    description_to = "Transfer to " + category.name
    description_from = "Transfer from " + self.name
    if self.check_funds(amount) is True:
      self.balance += -amount
      transfer_from = {"amount": -amount, "description": description_to}
      self.ledger.append(transfer_from)
      category.balance += amount
      transfer_to = {"amount": amount, "description": description_from}
      category.ledger.append(transfer_to)
      return True
    else:
      return False


  def check_funds(self, amount):
    return self.balance >= amount




def create_spend_chart(categories):
  totals = {}
  totals_by_cat = []
  grand_total = 0
  percents = []
  total_line = '---'*(len(categories))
  cat_names = []
  num_bars = []
  
  chart = 'Percentage spent by category\n'
  
  # for each category in list
  for cat in categories:
    ledger = cat.ledger
    total = 0
  
    # for each expense in ledger, if negative update running total per category
    for expense in ledger:
      if expense['amount'] < 0:
        total += abs((expense['amount']))
        totals_by_cat.append(total)
        grand_total += total
  
    # add category names to cat_names list
    cat_names.append(cat.name)

    # add category name, total withdrawals to totals dict
    totals[cat.name] = total

    # get percents by category and append to percents list
  for totals in totals_by_cat:
    percent = round(totals/grand_total, 3)
    percents.append(percent)

  # determine number of 'o' needed per category, append number to num_bars list
  for i in percents:
    bubbles = i//.01
    num_bars.append(int(bubbles))
  
  for number in range(100, -10, -10):
    chart += f"{number:3d}| "
    for percent in num_bars:
      if percent >= number:
        chart += 'o  '
      else:
        chart += '   '
  
    chart += '\n'
  
  # Create horizontal line
  line_space = len(total_line) + 2
  chart += f"  {total_line:>{line_space}}-\n"
  
  # Create vertical category names
  for i in itertools.zip_longest(*cat_names, fillvalue=' '):
    cats = '  '.join(i)
    chart += f"     {cats}  \n"
    
      
  
  return chart.rstrip('\n')
  