function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));
%display(size(Theta1_grad));
%display(size(Theta2_grad));


% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
a_1 = [ones(m, 1) X];
temp=sigmoid(a_1*Theta1');
temp = [ones(m, 1) temp];
htheta=sigmoid(temp*Theta2');
yk = [];
for K = 1:num_labels,
	yk = [yk y==K];
end
test=(-yk.*log(htheta))-((1-yk).*log(1-htheta));
J=J+sum(sum(test))/m;
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
delta3=(htheta-yk);
r2=delta3*Theta2;
delta2=(r2).* (temp.* (1 - temp));
delta2=delta2(:,2:end);
Theta1_grad=(Theta1_grad+(delta2' * a_1))*(1/m);
Theta2_grad=(Theta2_grad+(delta3'*temp))*(1/m);
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%
temp1=Theta1(:,2:end);
temp2=Theta2(:,2:end);
J=J+(lambda/(2*m))*(sum(sum(temp1.*temp1))+sum(sum(temp2.*temp2)));
t1=lambda.*Theta1;
t1(:,1)=0;
t2=lambda.*Theta2;
t2(:,1)=0;
Theta1_grad=Theta1_grad+t1*(1/m);
Theta2_grad=Theta2_grad+t2*(1/m);
%display(size(Theta1_grad));
%display(size(Theta2_grad));
% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];

end
