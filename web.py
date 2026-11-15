from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Network Protocols</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f9;
            margin: 030px;
        }

        h1 {
            text-align: center;
            color: #1e3a5f;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background-color: white;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #1e3a5f;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #eaf0f6;
        }

        tr:hover {
            background-color: #d6e8ff;
        }
    </style>
</head>
<body>

    <h1>List of Network Protocols</h1>

    <table>
        <tr>
            <th>S.No</th>
            <th>Protocol Name</th>
            <th>Port Number</th>
            <th>Purpose</th>
        </tr>

        <tr>
            <td>1</td>
            <td>HTTP</td>
            <td>80</td>
            <td>Transfers web pages</td>
        </tr>

        <tr>
            <td>2</td>
            <td>HTTPS</td>
            <td>443</td>
            <td>Secure web communication</td>
        </tr>

        <tr>
            <td>3</td>
            <td>FTP</td>
            <td>20, 21</td>
            <td>Transfers files</td>
        </tr>

        <tr>
            <td>4</td>
            <td>SSH</td>
            <td>22</td>
            <td>Secure remote login</td>
        </tr>

        <tr>
            <td>5</td>
            <td>Telnet</td>
            <td>23</td>
            <td>Remote login without encryption</td>
        </tr>

        <tr>
            <td>6</td>
            <td>SMTP</td>
            <td>25</td>
            <td>Sends emails</td>
        </tr>

        <tr>
            <td>7</td>
            <td>DNS</td>
            <td>53</td>
            <td>Converts domain names to IP addresses</td>
        </tr>

        <tr>
            <td>8</td>
            <td>DHCP</td>
            <td>67, 68</td>
            <td>Automatically assigns IP addresses</td>
        </tr>

        <tr>
            <td>9</td>
            <td>POP3</td>
            <td>110</td>
            <td>Retrieves emails</td>
        </tr>

        <tr>
            <td>10</td>
            <td>IMAP</td>
            <td>143</td>
            <td>Manages emails on a mail server</td>
        </tr>

        <tr>
            <td>11</td>
            <td>SNMP</td>
            <td>161, 162</td>
            <td>Monitors and manages network devices</td>
        </tr>

        <tr>
            <td>12</td>
            <td>NTP</td>
            <td>123</td>
            <td>Synchronizes system clocks</td>
        </tr>

        <tr>
            <td>13</td>
            <td>LDAP</td>
            <td>389</td>
            <td>Accesses directory services</td>
        </tr>

        <tr>
            <td>14</td>
            <td>RDP</td>
            <td>3389</td>
            <td>Remote desktop access</td>
        </tr>

        <tr>
            <td>15</td>
            <td>TFTP</td>
            <td>69</td>
            <td>Simple file transfer</td>
        </tr>
    </table>

</body>
</html>
"""
self.wfile.write(content.encode())
server_address = ('',88)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
