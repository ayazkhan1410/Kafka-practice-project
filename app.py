from producer import send_profile_event


target_url = input("Enter the target URL: ")
target_name = input("Enter the target name: ")

print(f"Target URL: {target_url}")
print(f"Target Name: {target_name}")

test_data = {
    "target_url": target_url,
    "target_name": target_name,
}

# Send profile event
print("================================================")
print("Sending profile event...")
send_profile_event(test_data)
print("================================================")
print("Profile event sent successfully")
print("================================================")
