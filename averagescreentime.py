import matplotlib.pyplot as plt

agegroups = ["0-2","2-8","8-13","14-18"]
screentime = [1.05,2.13,5.5,8.5]

plt.bar(agegroups, screentime, color='steelblue', edgecolor='navy', alpha=0.7)
plt.xlabel('Age Groups', fontsize=12, fontweight='bold')
plt.ylabel('Screen Time (hours)', fontsize=12, fontweight='bold')
plt.title('Average Screen Time by Age Group', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.show()
print("information from:")
print("AAP.ORG")
print("Average Amount of Screen Time for Children and Young Adults")
print("https://www.aap.org/en/patient-care/media-and-children/center-of-excellence-on-social-media-and-youth-mental-health/qa-portal/qa-portal-library/qa-portal-library-questions/average-amounts-of-screen-time/?srsltid=AfmBOoqEOjQVGJlCEb4Ck8N4j04XOPyoIi656WnTKYfdzHfZu9ey-pBU")