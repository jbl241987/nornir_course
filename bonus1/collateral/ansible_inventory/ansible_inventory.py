from nornir import InitNornir
from nornir_netmiko import netmiko_send_command


def main():
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(name="nxos1")
    agg_result = nr.run(
        task=netmiko_send_command, command_string="show run | i hostname"
    )
    print(agg_result["nxos1"].result)


if __name__ == "__main__":
    main()
