close all;
clear variables;

mat_img = imread('images/test.png');
sz = size(mat_img);
i_size = sz(1);
j_size = sz(2);
prc_img = zeros(i_size,j_size);
for i = 1:i_size
  for j = 1:j_size
    img_R = mat_img(i,j,1);
    img_G = mat_img(i,j,2);
    img_B = mat_img(i,j,3);
    if (img_R > 0) && (img_G > 0) && (img_B < 256)
      prc_img(i,j) = 0;
    else 
      prc_img(i,j) = 1;
    end
  end
end
imshow(prc_img);


% faire des tests à l'infini