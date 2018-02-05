function p = predict(theta, X)
% Predict whether the label is 0 or 1 using learned logistic regression 
% parameter theta
%    p = predict(theta, X) computes the predictions for X using a
%    threshold at 0.5 (i.e., if sigmoid(theta'*x) >= 0.5, predict 1)

m = size(X, 1); % Number of training example

p = zeros(m, 1);

%for it = 1:m
%  if (sigmoid(X(it,:) * theta) >= 0.5)
%    p(it) = 1;
%  else
%    p(it) = 0;
%  end
%end

% shorter code than above
p = sigmoid(X * theta);
p = p >= 0.5;

end