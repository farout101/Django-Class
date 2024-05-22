from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # dictionary
    #     print("cleaned_data: ", cleaned_data)
    #     title = cleaned_data.get("title")
    #     return title
    
    def clean(self):
        clean_data = self.cleaned_data
        
        print("clean_data: ", clean_data)
        
        return clean_data