% initialization
clear; close all; clc

%% =============== Part1: load data =================
data = load('train.txt');
X = data(:, [2,3,4,5,6,7]); y = data(:,1);

% no. of training examples & features
[m, n] = size(X);

% add intercept term to x
X = [ones(m,1) X];

% initialize fitting parameters
initial_theta = zeros(n + 1, 1);

%% =============== Part2: Compute cost function and gradient ==============
[cost, grad] = costFunction(initial_theta, X, y);


%% =============== Part3: Optimizing using fminunc ==================

options = optimset('Gradobj', 'on', 'MaxIter', 400);

% Run fminunc to obtain the optimal theta
% This function will return theta and the cost
[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);


%% =============== Part4: Predict ===================
data_test = load('test.txt');
X_test = data_test(:,[2,3,4,5,6,7]);
X_id = data_test(:,1);
m_test = size(X_test,1);
X_test = [ones(m_test,1) X_test];

p = predict(theta, X_test);

filename = "submission.csv";
fid = fopen(filename, "w");
fputs (fid, "PassengerId,Survived\n");

for it = 1:size(p)
  fprintf(fid, "%d,%d\n", X_id(it), p(it));
end

fclose(fid);
