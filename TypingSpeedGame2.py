import time

TARGET_TEXT = "Python is the best language"

print("Type the following sentence as fast as you can:\n")
print(TARGET_TEXT)

input("\nPress Enter to start...")
start_time = time.time()

user_input = input("\nStart typing:\n")
end_time = time.time()

time_taken = end_time - start_time

# Remove extra spaces for fair comparison
if user_input.strip() == TARGET_TEXT:
    print(f"\n✅ Correct!")
    print(f"⏱ Time taken: {time_taken:.2f} seconds")
else:
    print("\n❌ Incorrect text.")
    print(f"⏱ Time taken: {time_taken:.2f} seconds")


