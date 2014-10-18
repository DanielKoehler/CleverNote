
//
//  DetailedNoteViewController.m
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import "DetailedNoteViewController.h"

@interface DetailedNoteViewController ()

@end

@implementation DetailedNoteViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    
    
}

-(void) setNote:(Note *)note {
    
    [self setTitle:note.title];
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
