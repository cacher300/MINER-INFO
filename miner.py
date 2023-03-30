import discord
import requests

TOKEN = "OTY5MDUyNyNDg1MDI4ODY0.GJWl1_.-vfzuR0KpCbgAb3Xa2yskE9caItCJdqRmzXA"
PREFIX = "!"

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(PREFIX):
        command = message.content.split(" ")[0][1:].lower()
        if command == "accountbalance":
            await get_account_balance(message)
        elif command == "averagehashrate":
            await get_average_hashrate(message)
        elif command == "chartdata":
            await get_chart_data(message)
        elif command == "checkmineraccount":
            await check_miner_account(message)
        elif command == "currenthashrate":
            await get_current_hashrate(message)
        elif command == "generalinfo":
            await get_general_info(message)
        elif command == "hashratehistory":
            await get_hashrate_history(message)
        elif command == "lastreportedhashrate":
            await get_last_reported_hashrate(message)
        elif command == "listofworkers":
            await get_list_of_workers(message)
        elif command == "payments":
            await get_payments(message)
        elif command == "shareratehistory":
            await get_share_rate_history(message)
        elif command == "workersaveragehashrate":
            await get_workers_average_hashrate(message)
        elif command == "workerslastreportedhashrate":
            await get_workers_last_reported_hashrate(message)

async def get_account_balance(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/balance/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    balance = response.json()["data"]
    await message.channel.send("Account Balance: {}".format(balance))

async def get_average_hashrate(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/avghashratelimited/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3/24")
    avg_hashrate = response.json()["data"]
    await message.channel.send("Average Hashrate: {}".format(avg_hashrate))

async def get_chart_data(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/chart/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    chart_data = response.json()["data"]
    await message.channel.send("Chart Data: {}".format(chart_data))

async def check_miner_account(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/user/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    user_info = response.json()["data"]
    await message.channel.send("Miner Account Info: {}".format(user_info))

async def get_current_hashrate(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/hashrate/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    current_hashrate = response.json()["data"]
    await message.channel.send("Current Hashrate: {}".format(current_hashrate))

async def get_general_info(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/network")
    network_info = response.json()["data"]
    await message.channel.send("Network Info: {}".format(network_info))

async def get_hashrate_history(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/hashratehistory/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    hashrate_history = response.json()["data"]
    await message.channel.send("Hashrate History: {}".format(hashrate_history))


async def get_last_reported_hashrate(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/lastreport/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    last_reported_hashrate = response.json()["data"]
    await message.channel.send("Last Reported Hashrate: {}".format(last_reported_hashrate))

async def get_list_of_workers(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/workers/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    worker_list = response.json()["data"]
    await message.channel.send("List of Workers: {}".format(worker_list))

async def get_payments(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/payments/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    payment_info = response.json()["data"]
    await message.channel.send("Payment Info: {}".format(payment_info))

async def get_share_rate_history(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/shareratehistory/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    share_rate_history = response.json()["data"]
    await message.channel.send("Share Rate History: {}".format(share_rate_history))

async def get_workers_average_hashrate(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/workers/avghashrate/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    workers_avg_hashrate = response.json()["data"]
    await message.channel.send("Workers Average Hashrate: {}".format(workers_avg_hashrate))

async def get_workers_last_reported_hashrate(message):
    response = requests.get("https://api.nanopool.org/v1/xmr/workers/lastreport/49rqMUePnE1ge9LoayoLVv7Sf6MYj2GP3YJRTD6suG35DRBZixuVFVrCN811nJEqDY83yj5DQdhWyJbSFVbQZQPjNsAyfF3")
    workers_last_reported_hashrate = response.json()["data"]
    await message.channel.send("Workers Last Reported Hashrate: {}".format(workers_last_reported_hashrate))

client.run(TOKEN)
