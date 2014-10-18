//
//  NotesViewController.h
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "SignInViewController.h"

@interface NotesViewController : UIViewController <UITableViewDataSource, UITableViewDelegate>

@property (strong, nonatomic) UIViewController *signInViewController;

@property (strong, nonatomic) IBOutlet UITableView *notesView;

@property (strong, nonatomic) NSArray *notes;

@end

