import matplotlib.pyplot as plt

agegroups = [
    "0-2",
    "2-4",
    "5-8",
    "9-12",
    "13-15",
    "16-18",
    "19-24",
    "25-34",
    "35-49",
    "50+"
]


screentime = [
    0.5,
    1.0,
    2.25,
    4.5,
    8.5,
    9.0,
    8.5,
    7.0,
    6.0,
    5.0
]

if len(agegroups) != len(screentime):
    raise ValueError('agegroups and screentime must have the same number of entries')

plt.figure(figsize=(10, 6))
plt.bar(agegroups, screentime, color='steelblue', edgecolor='navy', alpha=0.7)
plt.xlabel('Age Groups', fontsize=12, fontweight='bold')
plt.ylabel('Average Daily Screen Time (hours)', fontsize=12, fontweight='bold')
plt.title('Estimated Average Daily Screen Time by Age Group', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.show()
print("information from:")
print("- AAP Media and Young Minds: https://www.aap.org/en-us/advocacy-and-policy/aap-health-initiatives/Pages/Media-and-Children.aspx")
print("- Common Sense Media Census: https://www.commonsensemedia.org/research/the-common-sense-census-media-use-by-tweens-and-teens-2021")
print("- Nielsen US screen time and media usage averages")
