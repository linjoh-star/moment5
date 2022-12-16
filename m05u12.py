import subprocess

# Ange startbalansen och räntan
balance = 10000
interest_rate = 0.03

# Öppna en fil för att skriva ut data
with open('account_data.txt', 'w') as f:
  # Loop över åren
  for year in range(1, 16):
    # Beräkna den årliga räntan
    interest = balance * interest_rate
    # Lägg till räntan till balansen
    balance += interest
    # Skriv ut data för det aktuella året
    f.write(f"År {year}: {balance:.2f}kr ({interest_rate * 100}%)\n")

# Öppna filen med subprocess.run()
subprocess.run(['open', 'account_data.txt'])
