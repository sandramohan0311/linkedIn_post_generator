import pandas as pd
import json

class FewShotPosts:
    def __init__(self, file_path="Data/processed_data.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding='utf-8') as file:
            posts = json.load(file)
            self.df = pd.json_normalize(posts)

            self.df["length"] = self.df["line_count"].apply(self.categorize_length)
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))
       
            self.df = self.df

            # print(f"✅ Loaded {len(self.df)} posts from {file_path}")
            # print("Columns:", self.df.columns.tolist())
            # print("Unique tags:", self.unique_tags)

    def categorize_length(self, line_count):
        if line_count < 5:
            return "short"
        elif 5 <= line_count <= 10:
            return "medium"
        else:
            return "long"
        

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self, length, language, tag):
        filtered_df = self.df[(self.df["length"] == length) & (self.df["language"] == language) & (self.df["tags"].apply(lambda x: tag in x))]
        return filtered_df.to_dict(orient='records')
    

   

if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("short","Hinglish","Career")
    print(posts)

    # print(fs.df.head())




