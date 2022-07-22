# Function to test RFmodel performance based on a range of max. no, of leaf node sizes

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):

    """
    The following function estimates mean absolute error as a metric for model
    accuracy.The number of trees used is set to 100 (i.e. n_estimators). 
    500 trees have also been tested but without any improvement in accuracy 
    so 100 is used to reduce training times.
    
    Parameters
    ----------
    max_leaf_nodes: str
        Number of the max no. of leaf nodes.
        
    train_X: array / list like
        Array of the variables to fit.
        
    train_y: array / list like
        Array of target values.
        
    val_X:
        Array of 'hold out' data not used in model training & therefore 
        available for model validation / checking / testing.
    
    val_y:
        Array of 'hold out' target values data not used in model training 
        & therefore available for model validation / checking / testing.
        
    """
    
    # Define the model
    model = RandomForestRegressor(max_leaf_nodes=max_leaf_nodes,
                                  random_state=1,
                                  n_estimators=100,
                                  n_jobs=-1)

    # Create a v simple pipeline that imputes missing input values before fitting the model to them
    #-----------------------------------------------------------------------------------------------
    my_pipeline = Pipeline(steps=[('preprocessor',
                                   SimpleImputer()), ('model', model)])

    # Calculate a metric variable using the cross_val_score function
    #----------------------------------------------------------------
    # The block below performs a cross validation excersise. For a given model configuration, it splits the
    # training set in 5 subsets and carries out a training sequence with the mean absolute error as a metric
    # of performance.
    # An avergae of those 5 MAE is then returned (see Figure below 'Validation' label).
    # This procedure ensures a robust training sequence as it removes the chance of
    # selecting a validation set that is very similar to the testing subset.
    #
    # Fit 5 random subsets of train_x & train_y to the pipeline RFR model & calc mean absolute error
    # multiply by -1 since sklearn calculates *negative* MAE
    metric = -1 * cross_val_score(
        my_pipeline, train_X, train_y, cv=5, scoring='neg_mean_absolute_error')

    # Train the model
    my_pipeline.fit(train_X, train_y)

    # Predict dependent variable using validation & training subsets of independent variables
    preds_val = my_pipeline.predict(val_X)
    preds_tr = my_pipeline.predict(train_X)

    # MAE calculation for training and validation data
    mae_ver = mean_absolute_error(val_y, preds_val)
    mae_tr = mean_absolute_error(train_y, preds_tr)

    # Bring it all together in outputs
    return (mae_ver, mae_tr, metric.mean())

if __name__ == '__main__':
    main()
    
