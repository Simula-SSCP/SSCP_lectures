% ExampleODE_sensitivity.m — Knockout Ymax sensitivity analysis

% Load baseline parameters
[params, y0] = ExampleODE_loadParams();
[rpar, tau, ymax, speciesNames] = params{:};
nSpecies = numel(y0);
nTimepoints = 40;
tspan = linspace(0, 4, nTimepoints);
results = zeros(nSpecies, nSpecies);  % rows: species, cols: knockout

% Baseline simulation
params_base = {rpar, tau, ymax, speciesNames};
[t, y_base] = ode15s(@(t, y) ExampleODE(t, y, params_base), tspan, y0);
y_base_final = real(y_base(end, :)');  % ensure real values

% Loop over each species
for i = 1:nSpecies
    ymax_perturbed = ymax;
    ymax_perturbed(i) = 0.5;  % Knock down this species
    % Create new param set
    perturbed_params = {rpar, tau, ymax_perturbed, speciesNames};
    % Simulate
    [t, y] = ode15s(@(t, y) ExampleODE(t, y, perturbed_params), tspan, y0);
    % Save final state for heatmap
    y_final = real(y(end, :)');  % final state, cleaned of roundoff
    % Avoid divide-by-zero with a small epsilon
    eps_val = 1e-12;
    relative_change = (y_final - y_base_final) ./ max(abs(y_base_final), eps_val);
    if isempty(y) || size(y,1) < 1
        warning("Simulation failed for KO %s", speciesNames{i});
        results(:, i) = NaN;
        continue;
    end
    results(:, i) = relative_change;
end
results = real(results); % suppresses an infinitessimal imaginary number float error
% Print numerical sensitivity matrix
disp('=== Sensitivity Results (Final Values) ===');
T = array2table(results, 'RowNames', speciesNames, 'VariableNames', matlab.lang.makeValidName(speciesNames));
disp(T);
% Plot heatmap of sensitivities
figure;
imagesc(results);
colorbar;
xlabel('Knocked-out input species');
ylabel('Measured species');
title('Relative change: (perturbed - base) / base');
set(gca, 'XTick', 1:nSpecies, 'XTickLabel', speciesNames, 'XTickLabelRotation', 45);
set(gca, 'YTick', 1:nSpecies, 'YTickLabel', speciesNames);