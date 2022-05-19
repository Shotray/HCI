# Lab 2: Information Retrieval

This project implements a user-friendly image category search function

## Installation

install conda environment

```
conda env create -f information_retrieval.yaml
conda activate myEnv
```

## Run

```
cd server
curl -o database.zip https://anjt.oss-cn-shanghai.aliyuncs.com/database.zip
unzip database.zip

python image_vectorizer.py
python rest_server.py 
```

## Requirements

Design and implement an image search system (interface) according to the Five-Stage Framework

The searching interface has the following features:

- It contains an input box to upload an image (Formulation);

- Users can preview the query image in the searching window (Formulation);

- It has a search button (Initiation);

- Provide an overview of the results (e.g. the total number of results) (Review);

- Allow changing search parameters (e.g. select certain category/tag) when reviewing results (Refinement);

- Users can take some actions, e.g. add selected images to a favorite list (Use);

- Other functions you would like to add in.

## Project Structure

```
└─server
    ├─database
    │  ├─dataset
    │  └─tags
    ├─imagenet
    │  └─classify_image_graph_def.pb
    ├─static
    │  ├─images
    │  └─result
    ├─templates
    │  └─main.html
    └─uploads
```

## ScreenShot

- Home Page

![image-20220519230001090](img/4.png)

- Search pictures

![image-20220519230054216](img/5.png)

![image-20220519234154298](img/7.png)

![image-20220519234259130](img/1.png)

![image-20220519234355139](img/8.png)

- Select tags

![image-20220519234421267](img/2.png)

![image-20220519234440167](img/3.png)

- Download pictures

![image-20220519234505182](img/6.png)

## Functions

- Formulation

  The project provide a input box to upload an image and users can preview the query image in the searching window.

  ```javascript
      $("#input-file").change(function () {
          const file = this.files[0];
          if (window.FileReader) {
              const reader = new FileReader();
              reader.readAsDataURL(file);
              console.log(reader);
              reader.onloadend = function (e) {
                  document.getElementById("searchimg").style.display = 'table';
                  document.getElementById("searchimg").src = e.target.result;
              };
          }
      });
  ```

  

- Initiation

  It has a search button

  ```html
  <input type=submit value="Search!" onclick="fun()">
  ```

- Review

  The project can provide an overview of the results, like the total number of results and all the pictures.

- Refinement

  User can select certain tag when reviewing results

  ```javascript
      $('.tags').click(function () {
          tag = document.getElementById(this.id).innerText;
          tagPics = []
          for(var idx in pythonResponse.image_list){
              if(pythonResponse.tag_list[idx] == tag) {
                  tagPics.push(pythonResponse.image_list[idx]);
              }
          }
          init();
          for (var idx in tagPics) {
              document.getElementById("img" + idx).src = tagPics[idx];
              document.getElementById("img" + idx).style.display="block";
              document.getElementById("download-pic" + idx).style.display="block";
          }
      })
  ```

- Use

  User can download pictures after searching

  ```javascript
      $('.download-pic').click(function () {
          const img = this.parentNode.children[0];
          const download = document.createElement('a');
          const event = new MouseEvent('click');
          download.download = '图片';
          download.href = img.src;
          download.dispatchEvent(event);
      })
  ```

  

