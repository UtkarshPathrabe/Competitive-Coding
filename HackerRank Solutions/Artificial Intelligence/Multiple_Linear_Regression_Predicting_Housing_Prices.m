C = strsplit(input('', 's'));
F = str2double(C(1, 1));
N = str2double(C(1, 2));
data = zeros(N, F + 1);
for i = 1 : N
    C = strsplit(input('', 's'));
    for j = 1 : F + 1
        data(i, j) = str2double(C(1, j));
    end
end
X = data(:, 1 : F);
y = data(:, F + 1);
m = length(y);
X = [ones(m, 1) X];
theta = pinv(X'*X)*(X'*y);
T = str2double(input('', 's'));
for i = 1 : T
    XTestData = ones(1, F + 1);
    C = strsplit(input('', 's'));
    for i = 2 : F + 1
        XTestData(1, i) = str2double(C(1, i - 1));
    end
    price = XTestData * theta;
    fprintf('%.2f\n', price);
end