# 🧬 T2D-Bioinformatics-Classification
Automated Bioinformatics Pipeline for Type 2 Diabetes RNA-Seq Data

## ⚙️ System Overview
هذا المستودع يحتوي على بايبلاين مؤتمت لاستخراج بيانات (RNA-Seq) الخاصة بمرض السكر من النوع الثاني من قاعدة بيانات NCBI SRA.

## 🚀 Installation & Setup 

### 1. Prerequisites
تأكد من تثبيت Python 3.8+ وأداة SRA Toolkit.

### 2. Environment Setup
git clone https://github.com/YourUsername/T2D-Bioinformatics-Classification.git
cd T2D-Bioinformatics-Classification
pip install -r requirements.txt

### 3. Execution
python download_real_data.py

> Note: تم ضبط النظام لسحب 5000 قراءة كإثبات فكرة لضمان سرعة التنفيذ.# T2D-Bioinformatics-Classification
*Documentation is currently being drafted by the technical writing team.*

## 📊 Data Quality Control (QC) & Clinical Validation
لضمان موثوقية البيانات لاستخدامها في خوارزميات التصنيف وتطبيقات تعلم الآلة (Machine Learning)، تم تطبيق المعايير السريرية التالية:

- Balanced Cohort (توازن العينات): تم اختيار 10 عينات متوازنة بعناية (5 لمرضى السكر T2D مقابل 5 أصحاء Healthy Controls) لمنع أي انحياز (Bias) في النماذج المستقبلية.
- Metadata Mapping (الربط الإكلينيكي): تم إنشاء ملف metadata.csv لربط المعرفات المبهمة (SRA IDs) بالحالة السريرية الفعلية لكل مريض، وهو الأساس لعمليات الـ Supervised Learning.
- Clinical Validity (الموثوقية السريرية): جميع العينات مستخرجة من دراسات موثقة على قاعدة بيانات NCBI، مما يضمن أن الـ Pipeline يستخرج بيانات بيولوجية حقيقية 100%.

---
