# Step-by-Step GitHub Setup - Starting from Proxmox Console

## Step 1: Access Ubuntu VM Console

1. Open Proxmox web interface: `https://192.168.2.100:8006`
2. In the left panel, click on **VM 101 (home-assistant)**
3. Click **Console** button (top right area)
4. You should see the Ubuntu login screen

## Step 2: Login to Ubuntu

**If you see a login prompt:**
- Try common usernames: `ubuntu`, `admin`, `homeassistant`, `user`
- Enter the password you set when you created the VM

**If you're already logged in (see a terminal prompt):**
- Perfect! Continue to Step 3

**If you can't remember the password:**
- We can reset it via Proxmox single-user mode (I'll guide you)

## Step 3: Find Your Username

Once logged in, run these commands:

```bash
# Show current username
whoami

# Show all users
cat /etc/passwd | grep -E '/home|/root' | cut -d: -f1

# Show who's logged in
who
```

**Copy the output and send it to me.**

## Step 4: Find Home Assistant Config Location

Run these commands:

```bash
# Check for docker-compose.yml files
sudo find / -name "docker-compose.yml" 2>/dev/null

# Or check running Docker containers
sudo docker ps

# Show Docker container details for HA
sudo docker inspect homeassistant 2>/dev/null | grep -A 10 Mounts

# Common locations to check
ls -la /opt/homeassistant/
ls -la ~/homeassistant/
ls -la /home/*/homeassistant/
```

**Copy the output and send it to me.**

## Step 5: Check if Git is Installed

```bash
git --version
```

If it says "command not found", we'll install it next.

---

## Quick Reference: What to Do Now

1. **Open Proxmox web UI** → VM 101 → Console
2. **Login** (try `ubuntu` or common usernames)
3. **Run Step 3 commands** → Copy output to me
4. **Run Step 4 commands** → Copy output to me
5. **I'll guide you** through the rest!

---

## If You Can't Login

If you don't know/remember the Ubuntu password, tell me and I'll show you how to:
1. Boot into recovery mode from Proxmox
2. Reset the password
3. Get back in and continue

**Start with Step 1 and let me know what you see!**
