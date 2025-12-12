# Monitoring Setup with Prometheus, Grafana, Node Exporter & Blackbox Exporter

This guide explains how to install **Grafana**, connect it with **Prometheus**, and import dashboards for **Node Exporter** and **Blackbox Exporter**. Screenshots have been included below.

---

## 🚀 1. Install Grafana on the Monitoring Server

Run the following commands on the server where Prometheus is already installed:

```bash
sudo apt-get install -y adduser libfontconfig1 musl
wget https://dl.grafana.com/grafana-enterprise/release/12.3.0/grafana-enterprise_12.3.0_19497075765_linux_amd64.deb
sudo dpkg -i grafana-enterprise_12.3.0_19497075765_linux_amd64.deb
```

---

## 🔓 2. Allow Port 3000 in AWS monitoring instance


---

## 🌐 3. Access Grafana in Browser

Open your browser and enter:

```
http://<public-ip>:3000/
```

Example:

```
http://13.232.121.58:3000/
```

Login with the default credentials:

* **Username:** admin
* **Password:** admin

You will be prompted to change the password.

---

## 🔗 4. Add Prometheus as a Data Source

1. Go to **Connections → Data sources**
2. Select **Prometheus**
3. Enter URL:

```
http://13.232.121.58:9090/
```

4. Click **Save & Test**

---

## 📊 5. Import Node Exporter Dashboard

1. Open the Grafana sidebar → **Dashboard → New → Import**
2. Search online for "Grafana Node Exporter Dashboard" (popular ID: **1860**)
3. Enter the dashboard ID
4. Select **Prometheus** as data source
5. Click **Import**

### 📸 Screenshot – Node Exporter Dashboard

![Node Exporter Dashboard](./node-exporter.png)

---

## 🧪 6. Import Blackbox Exporter Dashboard (Application Monitoring)

1. Go to **Dashboard → New → Import**
2. Search for "Grafana Blackbox Exporter Dashboard" (popular ID: **7587**)
3. Enter the ID
4. Select **Prometheus** as the data source
5. Click **Import**

### 📸 Screenshot – Blackbox Exporter Dashboard

![Blackbox Exporter Dashboard](./blackbox-exporter.png)

---

## ✅ Your Monitoring System Is Ready!

You now have:

* Prometheus collecting metrics
* Grafana visualizing the metrics
* Node Exporter monitoring server health
* Blackbox Exporter monitoring application endpoints

If you want, I can also generate diagrams or architecture flow for the README.
