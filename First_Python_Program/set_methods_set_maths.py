## Add methods
s = set({1, 3, 5, 7, 9})
s.add(11)
print(s)

## Remove methods
s.remove(7)
print(s)

# Remove something that is not on the sets will return a KeyError:
# s.remove(13)
# print(s)  

# For avoid error, we will use discard instead of remove:
s.discard(13)
print(s)

# Copy are the same with list
s1 = s.copy()
if s1 == s:
    print(True)
elif s1 is s:
    print(False)

# Clear all the elements in the set by .clear()
s1.clear()
s.clear()
print(s1, s)

print('*** *** *** *** ***')
### SET MATHS
### Eg: You are a teacher, and you have to teach 2 classes of Math class and Biology class, now you want to find out your students in 2 classes as set as:
maths_class = {'Nick', 'Oliver', 'Dieu Bang', 'Vinh Phuc', 'Thuy Trang', 'Gia Man'}
biology_class = {'Dieu Bang', 'Vinh Phuc', 'Huy Ly', 'Phu Quang', 'Truc Linh', 'Quyen Pham', 'Thuy Diem'}
### 1. Generate a set with all your unique students:
print(f'All the students that i have in 2 classes: {maths_class | biology_class}')

### 2. Generate a set with students who are in both classes:
print(f'All the students that study in these 2 classes: {maths_class & biology_class}')
